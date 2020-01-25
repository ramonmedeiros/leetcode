class Solution:
    def twoSum(self, nums, target: int):
        a = {}
        for index in range(len(nums)):
            comp = target - nums[index]
            if a.get(comp) is not None:
                return [a[comp], index]
            a[nums[index]] = index

print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3,2,4], 6))
