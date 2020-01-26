class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        leng = len(nums)
        while index < leng:
            if nums[index] == val:
                nums[index] = nums[leng - 1]
                nums[leng - 1] = val
                leng = leng -1
                continue
            index = index + 1
        print(leng)
        print(nums)
        return leng
assert Solution().removeElement([3,2,2,3], 3) == 2
assert Solution().removeElement([0,1,2,2,3,0,4,2], 2) == 5
