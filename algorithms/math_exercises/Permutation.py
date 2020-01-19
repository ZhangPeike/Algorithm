class Solution:
    def __init__(self):
        self.permutations = []

    def Permutate(self,data, index_start, select_data, target_num):
        if len(select_data) == target_num:  # 选择的元素已经够了，就输出并返回
            self.permutations.append(select_data.copy())
            return
        if index_start >= len(data):  # 没有元素选了而且还没够，也是直接返回
            return
        select_data.append(data[index_start])  # 选择当前元素
        self.Permutate(data, index_start + 1, select_data, target_num)
        select_data.pop()  # 别忘了从已选择元素中先删除
        self.Permutate(data, index_start + 1, select_data, target_num)  # 不选择当前元素
    def Result(self):
        return self.permutations


if __name__ == "__main__":
    data = [1, 2, 3,4]
    key = Solution()
    key.Permutate(data, 0, [], 2)
    print(key.Result())
