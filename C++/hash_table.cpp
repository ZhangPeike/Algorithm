#include "pk_hash.hpp"
#include <iostream>
#include <unordered_map>
#include <vector>
class Solution {
public:
  // TwoSum: find two elements so that their sum is target
  std::vector<int> GetIndex(const std::vector<int> &nums, const int target) {
    std::unordered_map<int, int> my_map;
    for (size_t i = 0; i < nums.size(); i++) {
      int cur_val = nums[i];
      int res = target - cur_val;
      auto iter = my_map.find(res);
      if (iter != my_map.end()) {
        return std::vector<int>({(int)i, iter->second});
      }
      my_map.insert(std::make_pair(cur_val, i));
    }
  };
  int GetLengthOfLongestSubString(const std::string &s) {
    // std::vector<int> m(256, -1);
    using namespace std;
    vector<int> m(256, -1);
    int res = 0, left = -1;
    for (int i = 0; i < s.size(); ++i) {
      std::cout << "time: " << i;
      left = max(left, m[s[i]]);
      std::cout << " left: " << left;
      m[s[i]] = i;
      std::cout << " i - left: " << i - left;
      res = max(res, i - left);
      std::cout << " res: " << res << std::endl;
    }
    return res;
  };
  int GetLengthOfLongestSubStringHash(const std::string &s) {
    // error: input " "
    // expected ans: 1, not 0
    int i;
    int n = s.length();
    // for current substring
    int currlen;
    // for current start
    int st = 0;
    // for max length substring
    int maxlen = 0;
    // for max length substring
    int start;
    std::unordered_map<char, int> pos;
    pos[s[0]] = 0;
    for (i = i; i < n; i++) {
      if (pos.find(s[i]) == pos.end()) {
        pos[s[i]] = i;
      } else {
        if (pos[s[i]] >= st) {
          currlen = i - st;
          if (maxlen < currlen) {
            maxlen = currlen;
            start = st;
          }
          st = pos[s[i]] + 1;
        }
        pos[s[i]] = i;
      }
    }
    if (maxlen < i - st) {
      maxlen = i - st;
      start = st;
    }
    return maxlen;
  };
};

int main(int argc, char **argv) {
  std::unordered_map<int, int> my_map;
  std::vector<int> test_nums({2, 7, 9});
  Solution solution;
  auto ans = solution.GetIndex(test_nums, 9);
  std::cout << ans[0] << " " << ans[1] << std::endl;
  std::string str = "pwwkew";
  std::cout << "pwwkew longest substring length: "
            << solution.GetLengthOfLongestSubString(str) << std::endl
            << solution.GetLengthOfLongestSubStringHash(str) << std::endl;
  int a = 1;
  int b = -1;
  std::cout << "\nstd::max(1, -1): " << std::max(a, b) << std::endl;
  std::cout << "std::max(0, -1): " << std::max(0, -1) << std::endl;
  return 0;
}