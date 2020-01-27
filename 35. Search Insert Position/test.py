class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        r = len(nums)
        if target>nums[r-1]:
            return r
        l=0 
        r = r-1
        while l<r:
            m = l+(r-l)/2;
            if target>nums[m]:
                l=m+1
            else:
                r=m
        return l
assert Solution().searchInsert([1,3,5,6], 5) == 2
assert Solution().searchInsert([1,3,5,6], 2) == 1
assert Solution().searchInsert([1,3,5,6], 7) == 4
assert Solution().searchInsert([1,3,5,6], 0) == 0
assert Solution().searchInsert([1,3,5], 5) == 2
assert Solution().searchInsert([1,3,4,6,7,10], 11) == 6

