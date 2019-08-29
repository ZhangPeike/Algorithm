#include <chrono>
#include <iostream>
auto TimeFuncInvocation = [](auto &&func, auto &&... params) {
  // timer start
  auto now = std::chrono::system_clock::now();
  std::forward<decltype(func)>(func)(std::forward<decltype(params)>(params)...);
  // timer stop
  auto then = std::chrono::system_clock::now();
  // std::cout << "time elapsed: " << then - now << std::endl;
};
int main() { return 0; }