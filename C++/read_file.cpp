#include <cstring>
#include <fstream>
#include <iostream>
int main(){
  const char file[] ="/home/zpk/A-Projects/msc_ceres/debug/1510000140269026000.txt";
  std::ifstream ifs(file);
  if(!ifs.is_open()){
    std::cout<<"File not open."<<std::endl;
    return -1;
  }
  std::string line;
  while(std::getline(ifs, line)){
    std::cout<<line<<std::endl;
  }
  return 0;
}
