#include <vector>
#include <string>
#include <iostream>

int main()
{
    std::vector<std::string> msg{"MinGW", "Hello", "World", "from", "VScode", "C++ extension"};
    for (auto x : msg)
    {
        std::cout << x << " ";
    }
    std::cout << std::endl;
    return 0;
}