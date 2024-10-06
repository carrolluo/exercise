class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(n):
            val = abs(nums[i])
            if val - 1 in range(0, n):
                if nums[val - 1] > 0:
                    nums[val - 1] = - nums[val - 1]
                elif nums[val - 1] == 0:
                    nums[val - 1] = - (n + 1)
        print(nums)
        for i in range(1, n + 1):
            if nums[i - 1] >= 0:
                return i
        return n + 1
