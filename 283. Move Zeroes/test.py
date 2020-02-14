class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        index = 0
        while index < l-1:
            if nums[index] != 0:
                index = index + 1
                continue

            swap = nums.pop(index)
            nums.insert(l, swap)
            l = l-1
        return nums

assert Solution().moveZeroes([0,1,0,3,12]) == [1,3,12,0,0]
assert Solution().moveZeroes([0,0,1]) == [1,0,0]
