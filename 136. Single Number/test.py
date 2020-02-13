class Solution(object):
   def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def deleteSimilar(nums, length):
            for index in range(1, length):
                if nums[0] == nums[index]:
                    nums.pop(index)
                    nums.pop(0)
                    return True
            return False

        l = len(nums)

        if l<=2:
            return nums[0]
        while l > 1:
            if deleteSimilar(nums, l) is False:
                break
            l = l - 2
            continue
        return nums[0]
assert Solution().singleNumber([1,0,1]) == 0
assert Solution().singleNumber([2,2,1]) == 1
assert Solution().singleNumber([4,1,2,1,2]) == 4
