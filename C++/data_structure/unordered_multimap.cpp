#include <iostream>
#include <tuple>
#include <unordered_map>
#include <utility>
using String = std::string;
using Phone = std::tuple<String, String, String>;
using Name = std::pair<String, String>;
class PhoneHash {
public:
  size_t operator()(const Phone &p) const {
    return std::hash<String>()(std::get<0>(p) + std::get<1>(p) + std::get<2>(p));
  }
};
std::unordered_multimap<Phone, Name, PhoneHash> by_phone{150, PhoneHash()};
std::istream &operator>>(std::istream &in, Phone phone) {
  String area_code{};
  String exchange_code{};
  String main_code{};
  in >> std::ws >> area_code >> exchange_code >> main_code;
  phone = std::make_tuple(area_code, exchange_code, main_code);
  return in;
}
// TODO: operator>> for Name

int main() {
  std::unordered_multimap<std::string, size_t> students;
  students.insert({"Jane", 0});
  students.emplace_hint(students.end(), "Jim", 1);
  for (auto x : students) {
    std::cout << "Name: " << x.first << " ID: " << x.second << std::endl;
  }
  return 0;
}