/*
    project euler, problem 11
    
    In the 20x20 grid in problem_11_data.txt, four numbers along a diagonal line have been marked in red. [(6, 8), (7, 9), (8, 10), (9, 11)].

    The product of these numbers is 26*63*78*14 = 1788696.
    What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid?
*/

/*
  Note that this solution wraps at the edges of the matrix.
*/

#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <ranges>
#include <utility>


auto readData(std::string path)
{
  //
  // Read text from file at path
  //
  std::vector<std::string> ret;
  std::ifstream ifs;
  std::string buf;
  ifs.open(path, std::ios::in);
  if(ifs){
    while(!ifs.eof()){
      getline(ifs, buf);
      if(!buf.empty()){
	ret.push_back(buf);
      }
    }
    ifs.close();
  }
  return ret;
}

namespace parsing{
  auto to_string = [](auto&& r) -> std::string
  {
    const auto data = &*r.begin();
    const auto size = static_cast<size_t>(std::ranges::distance(r));
    return std::string{data, size};
  };

  auto split(const std::string& str, char delimiter) -> std::vector<std::string>
  {
    const auto range = str |
      std::ranges::views::split(delimiter) |
      std::ranges::views::transform(to_string);

    return {std::ranges::begin(range), std::ranges::end(range)};
  }

  void parseData(const std::vector<std::string> data, std::vector<std::vector<int> >& mat)
  {
    //
    // parse data and create 2-d matrix
    //
    std::vector<std::string> row;
    std::vector<int> rowi;
    for(auto l : data){
      rowi = {};
      row = split(l, ' ');
      std::transform(row.begin(), row.end(), std::back_inserter(rowi), [](const std::string& s){return std::stoi(s);} );
      mat.push_back(rowi);
    }
  }
}


typedef std::vector<std::pair<int, int> > indexes;
typedef std::vector<std::vector<int> >::size_type MatSize;

indexes saveIndexes(const int r0, const int c0, const int r1, const int c1, const int r2, const int c2, const int r3, const int c3)
{
  //
  // Return a vector of coordinate pairs
  //
  return {
    std::pair<int, int>(r0, c0),
    std::pair<int, int>(r1, c1),
    std::pair<int, int>(r2, c2),
    std::pair<int, int>(r3, c3),
  };
}


std::pair<int, indexes> getMaxH(std::vector<std::vector<int> > mat)
{
  //
  // Return the max horizontal product of 4 elements in a row in mat
  //
  indexes coords = saveIndexes(0, 0, 0, 1, 0, 2, 0, 3);
  int max = mat[0][0] * mat[0][1] * mat[0][2] * mat[0][3];
  for(MatSize row = 0; row < mat.size(); ++row){
    for(MatSize col = 0; col < mat.size() - 4; ++col){
      auto prod = mat[row][col] * mat[row][col + 1] * mat[row][col + 2] * mat[row][col + 3];
      if(prod > max){
	max = prod;
	coords = saveIndexes(row, col, row, col + 1, row, col + 2, row, col + 3);
      }
    }
  }
  return {max, coords};
}


std::pair<int, indexes> getMaxV(std::vector<std::vector<int> > mat)
{
  //
  // Return the max vertical product of 4 elements in a column in mat
  //
  indexes coords = saveIndexes(0, 0, 1, 0, 2, 0, 3, 0);
  int max = mat[0][0] * mat[1][0] * mat[2][0] * mat[3][0];
  for(MatSize col = 0; col < mat.size(); ++col){
    for(MatSize row = 0; row < mat.size() - 4; ++row){
      auto prod = mat[row][col] * mat[row + 1][col] * mat[row + 2][col] * mat[row + 3][col];
      if(prod > max){
	max = prod;
	coords = saveIndexes(row, col, row + 1, col, row + 2, col, row + 3, col);
      }
    }
  }
  return {max, coords};
}


void enforceNDiagBoundaries(const int matSize, int& rIndex, int& cIndex)
{
  //
  // Enforce matrix boundaries on element indexes,
  // when checking indexes on negative-slope diagonals
  //
  if(cIndex >= matSize){
    cIndex = cIndex - matSize;
  }
  if(rIndex >= matSize){
    rIndex = rIndex - matSize;
  }
}


void enforcePDiagBoundaries(const int matSize, int& rIndex, int& cIndex)
{
  //
  // Enforce matrix boundaries on element indexes,
  // when checking indexes on positive-slope diagonals
  //
  if(rIndex < 0){
    rIndex = rIndex + matSize;
  }
  if(cIndex >= matSize){
    cIndex = cIndex - matSize;
  }
}


std::pair<int, indexes> getMaxD(std::vector<std::vector<int> > mat)
{
  //
  // Return the max diagonal product of 4 elements in a diagonal in mat
  //
  indexes coords = saveIndexes(0, 0, 1, 1, 2, 2, 3, 3);
  int max = mat[0][0] * mat[1][1] * mat[2][2] * mat[3][3];
  int r0 = 0;
  int c0 = 0;
  int r1 = 0;
  int c1 = 0;
  int r2 = 0;
  int c2 = 0;
  int r3 = 0;
  int c3 = 0;
  // check negative-slope diagonals
  for(MatSize row = 0; row < mat.size(); ++row){
    for(MatSize col = 0; col < mat.size(); ++col){
      r0 = row;
      c0 = col;
      r1 = row + 1;
      c1 = col + 1;
      r2 = row + 2;
      c2 = col + 2;
      r3 = row + 3;
      c3 = col + 3;
      enforceNDiagBoundaries(mat.size(), r1, c1);
      enforceNDiagBoundaries(mat.size(), r2, c2);
      enforceNDiagBoundaries(mat.size(), r3, c3);
      auto prod = mat[r0][c0] * mat[r1][c1] * mat[r2][c2] * mat[r3][c3];
      if(prod > max){
	max = prod;
	coords = saveIndexes(r0, c0, r1, c1, r2, c2, r3, c3);
      }
    }
  }
  // check positive-slope diagonals
  for(MatSize row = 0; row < mat.size(); ++row){
    for(MatSize col = 0; col < mat.size(); ++col){
      r0 = row;
      c0 = col;
      r1 = row - 1;
      c1 = col + 1;
      r2 = row - 2;
      c2 = col + 2;
      r3 = row - 3;
      c3 = col + 3;
      enforcePDiagBoundaries(mat.size(), r1, c1);
      enforcePDiagBoundaries(mat.size(), r2, c2);
      enforcePDiagBoundaries(mat.size(), r3, c3);
      auto prod = mat[r0][c0] * mat[r1][c1] * mat[r2][c2] * mat[r3][c3];
      if(prod > max){
	max = prod;
	coords = saveIndexes(r0, c0, r1, c1, r2, c2, r3, c3);
      }
    }
  }
  return {max, coords};
}


bool sortResults(std::pair<int, indexes> r1, std::pair<int, indexes> r2)
{
  //
  // Sort results by max product, greatest to least
  //
  return r1.first > r2.first;
}


int main()
{
  std::string data_fn = "problem_11_data.txt";
  std::vector<std::string> data = readData(data_fn);
  for(auto s : data){
    std::cout << s << std::endl;
  }
  std::vector<std::vector<int> > mat;
  parsing::parseData(data, mat);
  auto maxH = getMaxH(mat);
  std::cout << "max H: " << maxH.first << std::endl;
  std::cout << "horizontal coords: " << std::endl;
  for(auto coord : maxH.second){
    std::cout << coord.first << " : " << coord.second << std::endl;
  }
  auto maxV = getMaxV(mat);
  std::cout << "max V: " << maxV.first << std::endl;
  std::cout << "vertical coords: " << std::endl;
  for(auto coord : maxV.second){
    std::cout << coord.first << " : " << coord.second << std::endl;
  }
  auto maxD = getMaxD(mat);
  std::cout << "max D: " << maxD.first << std::endl;
  std::cout << "diagonal coords: " << std::endl;
  for(auto coord : maxD.second){
    std::cout << coord.first << " : " << coord.second << std::endl;
  }
  std::vector<std::pair<int, indexes> > results = {maxH, maxV, maxD};
  std::sort(results.begin(), results.end(), sortResults);
  std::cout << "absolute max: " << results[0].first << std::endl;
  std::cout << "coords: " << std::endl;
  for(auto coord : results[0].second){
    std::cout << coord.first << " : " << coord.second << std::endl;
  }  
}