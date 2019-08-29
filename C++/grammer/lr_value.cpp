#include <iostream>
void ProcessRValue(int &&rv) {}
struct AB {
  /* data */
  AB() {
    a_ = -1;
    b_ = -2;
  }
  AB(int a, int b) : a_(a), b_(b) {}
  int a_;
  int b_;
};

AB &SumOrigin(AB &x, const AB &y) {
  x.a_ = x.a_ + y.a_;
  x.b_ = x.b_ + y.b_;
  return x;
}
AB &Sum(const AB &x, const AB &y) {
  // without static AB it is error.
  static AB sum;
  sum.a_ = x.a_ + y.a_;
  sum.b_ = x.b_ + y.b_;
  return sum;
}

void swapp(int *a, int *b) {
  int temp;
  temp = *a;
  *a = *b;
  *b = temp;
}

void swapr(int &a, int &b) {
  int temp;
  temp = a;
  a = b;
  b = temp;
}
void swapv(int a, int b) {
  int temp;
  temp = a;
  a = b;
  b = temp;
}

int main() {
  int cnt = 99;
  double &&right_ref = 99 + 1;
  double &&right_ref_new = 2.0 * 1;
  std::cout << right_ref << " " << right_ref_new << std::endl;
  int a = 0;
  int b = 9;
  std::cout << "Using ptr to swap" << std::endl;
  swapp(&a, &b);
  std::cout << "Result,a: " << a << "b:" << b << std::endl;
  a = 0;
  b = 9;
  std::cout << "Using ref to swap" << std::endl;
  a = 0;
  b = 9;
  swapr(a, b);
  std::cout << "Result,a: " << a << "b:" << b << std::endl;
  a = 0;
  b = 9;
  swapv(a, b);
  std::cout << "Using value to swap" << std::endl;
  std::cout << "Result,a: " << a << "b:" << b << std::endl;
  std::cout << "------" << std::endl;
  AB x(1, 9);
  AB y(5, 8);
  AB sum_ok = SumOrigin(x, y);
  std::cout << "AB sum_ok: " << sum_ok.a_ << " " << sum_ok.b_ << std::endl;
  AB sum_error = Sum(x, y);
  std::cout << "AB sum_error: " << sum_error.a_ << " " << sum_error.b_ << std::endl;
  return cnt;
}