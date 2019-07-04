#include <array>
#include <cstring>
#include <iostream>
// for typeid
#include <typeinfo>
#include <vector>
// TODO： 程序退出后 new 占用内存是否会被清理
template <typename T, std::size_t N>
constexpr std::size_t ArraySize(T (&)[N]) noexcept {
  return N;
}

class Widget {
private:
  int length_;
  int *data_;
  //   static int cnt_ = 0;

public:
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
  Widget(Widget &&other) : data_(nullptr), length_(0) {
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
  std::vector<int> d(6, 1);
  AuthenticateAndAccessLvalue(d, 5) = 100;
  std::cout << "d[5]: " << d[5] << std::endl;
  std::vector<Widget> vec_Widget;
  std::cout << "typeid(x).name(): " << typeid(vec_Widget).name() << std::endl;
  int n = 1;
  // bad
  std::cout << "type: " << typeid(n).name() << std::endl;
  // Widget w1(9);
  // vec_Widget.push_back(Widget(9));
  Widget w = Widget(9);
  // Widget w2(10);
  // vec_Widget.push_back(std::move(w2));
  // Widget w3(11);
  // std::cout << "look at =" << std::endl;
  // Widget w4;
  // w4 = Widget(12);
  // emplace_back is amazing
  // vec_Widget.emplace_back(std::move(w3));
  int vals[] = {1, 2, 3, 4, 5, 6, 7};
  std::array<int, ArraySize(vals)> mapped_vals;
  std::cout << "size: " << mapped_vals.size() << std::endl;
  auto x1 = 29;
  auto x2(29);
  auto x3{29};
  auto x4 = {29};

  return 0;
}