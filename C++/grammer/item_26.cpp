#include <iostream>
#include <set>
std::multiset<std::string> names;
std::string NameFromId(int id) {
  if (id < 0) {
    return "";
  } else {
    return "human";
  }
}
template <typename T> void LogAddImpl(T &&name, std::false_type) {
  names.emplace(std::forward<T>(name));
}
template <typename T> void LogAdd(T &&name) {
  LogAddImpl(std::forward<T>(name),
             std::is_integral<typename std::remove_reference<T>::type>());
}
void LogAddImpl(int id, std::true_type) { LogAdd(NameFromId(id)); }
class Person {
public:
  template <typename T> explicit Person(T &&n) : name_(std::forward<T>(n)) {}
  explicit Person(Person &p) : name_(std::forward<std::string &>(p.name_)) {
    std::cout << "Transfer." << std::endl;
  }
  explicit Person(std::string name) : name_(name) {
    std::cout << "Copy cotr by val" << std::endl;
  }
  //   right-hand-side
  explicit Person(const Person &rhs) : name_(rhs.name_) {
    std::cout << "Copy cotr." << std::endl;
  }
  //   find by id
  explicit Person(int idx);

private:
  std::string name_;
};
int main() {
  Person p("Jack");
  auto CloneP(p);
  const Person k("Nancy");
  auto CloneK(k);
  return 0;
}