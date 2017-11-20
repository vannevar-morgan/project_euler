#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
#include <string>

using namespace std;
using namespace boost::multiprecision;

/*
PROBLEM STATEMENT:

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

The 12th term, F12 = 144, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
 */

cpp_int get_fib_n_digits(int& fib_count, const int digits);


int main(int argc, char* argv[]){
  string USAGE_MSG = "./p25 (digits [2-5000])";
  int digits = 1000;
  if(argc > 2){
    cout << USAGE_MSG << endl;
    return 0;
  }
  if(argc == 2){
    int temp = stoi(argv[1]);
    if(temp >= 2 && temp <= 5000){
      digits = temp;
    }else{
      cout << USAGE_MSG << endl;
      return 0;
    }
  }
  cout << "first term of the fibonacci sequence with " << digits << " digits:" << endl;
  int count = 0;
  cpp_int fib_n = get_fib_n_digits(count, digits);
  cout << "\nit's fib(" << count << ")...\n" << endl;
  cout << fib_n << endl;
  
  return 0;
}

cpp_int get_fib_n_digits(int& fib_count, const int digits = 1000){
  cpp_int fib_1 = 1;
  cpp_int fib_2 = 1;
  cpp_int fib_n = 0;
  fib_count += 2;
  while(true){
    fib_n = fib_2 + fib_1;
    fib_1 = fib_2;
    fib_2 = fib_n;
    ++fib_count;
    if(fib_n.str().size() >= digits){
      break;
    }
  }
  return fib_n;
}
