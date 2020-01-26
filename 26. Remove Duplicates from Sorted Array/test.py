class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        while index < len(nums) - 1:
            
            # no equal number, keep going
            if nums[index] != nums[index+1]:
                index = index +1
                continue
            
            nums.pop(index+1)
        return index+1

assert Solution().removeDuplicates([1,1,2]) == 2
assert Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
