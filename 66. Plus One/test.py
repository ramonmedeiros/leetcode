class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index = len(digits) -1

        import pdb;pdb.set_trace()
        while index >= 0:
            if digits[index] < 9:
                digits[index] = digits[index] + 1
                break
            digits[index] = 0
            if index == 0:
                digits.insert(0, 1)
                break
            index = index -1
        return digits

assert Solution().plusOne([1,2,3]) == [1,2,4]
assert Solution().plusOne([4,3,2,1]) == [4,3,2,2]
