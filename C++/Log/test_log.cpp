#include "log.hpp"
int main() {
  std::cout << "Test log." << std::endl;
  std::cout << "Log init: " << zpk::LogInit() << std::endl;
  // LOG("Hello world!");
  LOG("Hello world");
  return 0;
}