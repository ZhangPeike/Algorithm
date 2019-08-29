#include <algorithm>
#include <array>
#include <cstring>
#include <eigen3/Eigen/Core>
#include <iostream>
// for typeid
#include <typeinfo>
#include <vector>
// constexpr 编译期可用
template <typename T, std::size_t N>
constexpr std::size_t ArraySize(T (&)[N]) noexcept {
  return N;
}
void ProcessWidget(const bool IsHighPriority) {
  if (IsHighPriority) {
    std::cout << "VIP" << std::endl;
  } else {
    std::cout << "NOT VIP" << std::endl;
  }
}
// 右值引用与转移语义
class Widget {
private:
  int length_;
  int *data_;
  // 代理类: std::vector<bool>::reference
  std::vector<bool> vec_bool_{true, false};
  //   static int cnt_ = 0;
  std::string str_;

public:
  // decltype(auto) VecBool() { return std::forward<std::vector<bool>>(vec_bool_[1]);
  // };
  decltype(auto) GetVecBool() { return vec_bool_; }
  Widget() {
    length_ = 0;
    data_ = nullptr;
    // ++cnt_;
    std::cout << "ctor default" << std::endl;
  }
  Widget(int length) : length_(length), data_(new int[length]) {
    // ++cnt_;
    std::cout << "ctor para " << length_ << std::endl;
  }
  Widget(const Widget &other) : length_(other.length_), data_(new int[other.length_]) {
    std::copy(other.data_, other.data_ + length_, data_);
    std::cout << "Copy ctor." << std::endl;
  }
  Widget &operator=(const Widget &other) {
    std::cout << "Copy assignment operator." << std::endl;
    length_ = other.length_;
    if (data_ != nullptr) {
      delete[] data_;
    }
    data_ = new int[other.length_];
    memcpy(data_, other.data_, other.length_);
    return *this;
  }
  Widget(Widget &&other) : str_(std::move(other.str_)), data_(nullptr), length_(0) {
    data_ = other.data_;
    length_ = other.length_;
    other.data_ = nullptr;
    other.length_ = 0;
    std::cout << "Move ctor." << std::endl;
  }
  Widget &operator=(Widget &&other) {
    std::cout << "Move assignment operator." << std::endl;
    data_ = other.data_;
    other.data_ = nullptr;
    length_ = other.length_;
    other.length_ = 0;
    return *this;
  }
  ~Widget() {
    if (data_) {
      delete[] data_;
    };
    std::cout << "Default dctor" << std::endl;
  }
};
// how should I use it.
auto Less = [](const auto &p1, const auto &p2) { return *p1 < *p2; };
auto Print = [](const auto &p) { std::cout << p << std::endl; };
// Error
// auto CreateList() { return {1, 2, 3}; }
std::initializer_list<int> CreateList() { return {1, 2, 3}; }
// auto 作为函数返回值，采用模板型别推导, 如何避免复制
template <typename Container, typename Index>
decltype(auto) AuthenticateAndAccessLvalue(Container &c, Index i) {
  // do authenticat
  return c[i];
}
// 对于左右值均可以, C++14
template <typename Container, typename Index>
decltype(auto) AuthenticateAndAccess(Container &c, Index i) {
  return std::forward<Container>(c[i]);
}
int main() {
  // Eigen Matrix 是隐形代理类吗
  Eigen::Matrix2d m1;
  m1(0, 0) = 5;
  m1(1, 0) = 5;
  m1(0, 1) = 5;
  m1(1, 1) = 5;
  Eigen::Matrix2d m2 = Eigen::Matrix2d::Ones();
  auto m = m1 + m2;
  std::cout << "Type of eigen matrix sum: " << typeid(m).name() << std::endl;
  std::vector<int> d(6, 1);
  // std::for_each(d.begin(), d.end(), [](auto &x) { std::cout << x << " "; });
  std::for_each(d.begin(), d.end(), Print);
  AuthenticateAndAccessLvalue(d, 5) = 100;
  std::cout << "d[5]: " << d[5] << std::endl;
  std::vector<Widget> vec_Widget;
  std::cout << "typeid(x).name(): " << typeid(vec_Widget).name() << std::endl;
  int n = 1;
  // bad
  std::cout << "type: " << typeid(n).name() << std::endl;
  Widget w1(9);
  vec_Widget.push_back(Widget(9));
  Widget w = Widget(9);
  // Error result
  ProcessWidget(w.GetVecBool()[0]);
  // vector<bool> 取出的元素还是bool吗
  auto Priority = w.GetVecBool()[0];
  ProcessWidget(Priority);
  // Error result
  auto PriorityNew = static_cast<bool>(w.GetVecBool()[0]);
  ProcessWidget(PriorityNew);
  Widget w2(10);
  vec_Widget.push_back(std::move(w2));
  Widget w3(11);
  Widget w4;
  w4 = Widget(12);
  // emplace_back is amazing
  vec_Widget.emplace_back(std::move(w3));
  int vals[] = {1, 2, 3, 4, 5, 6, 7};
  std::array<int, ArraySize(vals)> mapped_vals;
  std::cout << "size: " << mapped_vals.size() << std::endl;
  auto x1 = 29;
  auto x2(29);
  auto x3{29};
  // x4的型别是什么？
  auto x4 = {29};
  return 0;
}