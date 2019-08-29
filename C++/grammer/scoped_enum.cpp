#include <cstdint>
#include <iostream>
// #include <string>
#include <tuple>
enum class Status : std::uint32_t { good, bad, indetermined = 0xffffffff };
// Web Interactivity
enum class UserInfoFields { uiName, uiEmail, uiReputation };
using UserInfo = std::tuple<std::string, std::string, int>;
template <typename E> constexpr auto GetIndex(E enumerator) noexcept {
  // std::underlying_type_t = std::underlying_type::type
  return static_cast<std::underlying_type_t<E>>(enumerator);
}
int main() {
  //   TODO: debug
  UserInfo ui("zhangpeike", "zhangpeike@youtube.com", 1);
  auto val = std::get<GetIndex(UserInfoFields::uiEmail)>(ui);
  std::cout << "email: " << val << std::endl;
  return 0;
}