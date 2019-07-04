#include <iostream>
#include <memory>
#include <string>
#include <typeinfo>
template <class T> std::string type_name() {
  typedef typename std::remove_reference<T>::type TR;
  std::unique_ptr<char, void (*)(void *)> own(
    // #ifndef _MSC_VER
    //     abi::__cxa_demangle(typeid(TR).name(), nullptr, nullptr, nullptr),
    // #else
    nullptr,
    // #endif
    std::free);
  std::string r = own != nullptr ? own.get() : typeid(TR).name();
  if (std::is_const<TR>::value)
    r += " const";
  if (std::is_volatile<TR>::value)
    r += " volatile";
  if (std::is_lvalue_reference<T>::value)
    r += "&";
  else if (std::is_rvalue_reference<T>::value)
    r += "&&";
  return r;
}
int &&Foo_Rref();
// template <class T> std::string type_name();
// int main() {
//   const double n = 9;
//   decltype(n) m = 10;
//   std::cout << "m: " << m << ", its type: " << type_name<decltype(m)>() <<
//   std::endl; std::cout << "m: " << m << ", its type: " << type_name<decltype((m))>()
//   << std::endl; std::cout << "Foo_Rref(): " << type_name<decltype(Foo_Rref())>() <<
//   std::endl;
//   //   std::cout << type_name<decltype(n)>() << std::endl;
//   return 0;
// }