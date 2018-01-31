#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/log/trivial.hpp>
#include <boost/log/expressions.hpp>
#include <string>
#include <map>
#include <utility>

using namespace std;
using namespace boost::multiprecision;

/*
PROBLEM STATEMENT:

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

The 12th term, F12 = 144, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
*/


/*
the naive version of this (problem_25.cpp) checks if fib_n.str().size() >= digits, for each fib(n)
which is an expensive operation (worsening as digits increase).

this version uses a binary search to find the nth fibonacci with the given number of digits.

you can increase (or decrease for a smaller table) the value of FIB_MAX to compute a larger fibonacci table
but consider that the fibonacci sequence increases exponentially.
increasing FIB_MAX will be more expensive with increasing fib(n)
(large fib(n) have > thousands of digits, it will require lots of memory to store the table)

alternatively you could implement a different strategy for computing fibonacci numbers
passing fib(n-1), fib(n-2) and computing smaller tables as needed

for very large numbers you might consider doing away with the table pre-compute and 
use a binary search strategy computing fib(n) = fib(n-1) + fib(n-2) as needed, 
doubling n until number of digits exceeds specified, then halving the range until the fibonacci
with specified number of digits is found.
at each doubling, save the fib(n) and fib(n+1) so the sequence can be recomputed from that point
in the sequence rather than recomputing the entire sequence.
additionally, as you compute fib(2n), save the fib(1.5n) and fib(1.5n + 1) (the mid), so the sequence
can be recomputed here without first needing to recompute mid.
*/
typedef unsigned int uint;
const static uint FIB_MAX = 100000; // fibonacci table size, max number of fibonacci elements to pre-compute

typedef map<int, cpp_int>::size_type map_sz;
pair<int, cpp_int> get_fib_n_digits(const int digits = 1000);
pair<int, cpp_int> bin_find_fib_map(map<int, cpp_int>& fib_map, const uint digits, const map_sz range_beg = 0, const map_sz range_end = 0, const bool range_indicated = false);
map<int, cpp_int> calc_fib(const uint fib_n = FIB_MAX);


void init_logging(){
  boost::log::core::get()->set_filter
    (boost::log::trivial::severity >= boost::log::trivial::info);
}

int main(int argc, char* argv[]){
  init_logging();
  string USAGE_MSG = "./p25 (digits [1-20899])";
  int digits = 1000;
  if(argc > 2){
    cout << USAGE_MSG << endl;
    return 0;
  }
  if(argc == 2){
    int temp = stoi(argv[1]);
    if(temp >= 1 && temp <= 20899){
      digits = temp;
    }else{
      cout << USAGE_MSG << endl;
      return 0;
    }
  }

  pair<int, cpp_int> fib_n = get_fib_n_digits(digits);
  BOOST_LOG_TRIVIAL(info) << "finished bin_find()..." << endl;

  if(fib_n.first == 0){
    cout << "specified number of digits is too great..." << endl;
    cout << "there may be a fib(n) with " << digits << " digits but it's greater than the the maximum fibonacci for the table of fibonacci numbers searched" << endl;
  }else{
    cout << "first term of the fibonacci sequence with " << digits << " digits:" << endl;  
    cout << "\nit's fib(" << fib_n.first << ")...\n" << endl;
    cout << fib_n.second << endl;
  }
  
  return 0;
}

pair<int, cpp_int> get_fib_n_digits(const int digits){
  //
  // return the first element of the fibonacci sequence with num digits >= specified num digits
  //
  BOOST_LOG_TRIVIAL(info) << "creating fib_table..." << endl;
  map<int, cpp_int> fib_map = calc_fib();
  BOOST_LOG_TRIVIAL(info) << "table size: " << fib_map.size() << endl;
  BOOST_LOG_TRIVIAL(info) << "doing bin_find()..." << endl;
  return bin_find_fib_map(fib_map, digits);
}

pair<int, cpp_int> bin_find_fib_map(map<int, cpp_int>& fib_map, const uint digits, const map_sz range_beg, const map_sz range_end, const bool range_indicated){
  //
  // perform binary find on fib_map to find the first element with num digits >= digits
  //
  pair<int, cpp_int> ret(0, 0);
  if(fib_map.empty()){
    return ret;
  }
  uint fibn_digits = 0;
  
  map_sz beg = 0;
  map_sz end = fib_map.size();
  map_sz n;
  if(range_indicated){
    beg = range_beg;
    end = range_end;
  }
  while(beg != end){
    n = beg + (end - beg) / 2;
    BOOST_LOG_TRIVIAL(debug) << "beg: " << beg << "\tmid: " << n << "\tend: " << end << endl;
    fibn_digits = fib_map[n].str().size();
    if(fibn_digits == digits){
      // search range before n for FIRST element with fibn_digits == digits
      pair<int, cpp_int> temp_ret = bin_find_fib_map(fib_map, digits, beg, n, true);
      if(temp_ret == ret){
	return pair<int, cpp_int>(n, fib_map[n]);
      }else{
	return temp_ret;
      }
    }else if(fibn_digits > digits){
      // search range before n
      end = n;
    }else{
      // search range after n
      beg = n + 1;
    }
  }
  return ret;
}

map<int, cpp_int> calc_fib(const uint n){
  //
  // return a table of fibonacci numbers [fib(1), fib(n)]
  // if n > FIB_MAX then the table returned is [fib(1), fib(FIB_MAX)]
  // if n <= 2 then the table returned is [fib(1), fib(2)]
  //
  map<int, cpp_int> fib_map;
  cpp_int fib_1 = 1;
  cpp_int fib_2 = 1;
  fib_map[1] = fib_1;
  fib_map[2] = fib_2;
  if(n <= 2){
    return fib_map;
  }
  int i = 2;
  cpp_int fib_n = 0;
  int fib_count = n > FIB_MAX ? FIB_MAX : n;
  while(i < fib_count){
    ++i;
    fib_n = fib_2 + fib_1;
    fib_1 = fib_2;
    fib_2 = fib_n;
    fib_map[i] = fib_n;
  }
  return fib_map;
}
