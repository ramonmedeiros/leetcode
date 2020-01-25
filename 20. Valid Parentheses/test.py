class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        expecting = []
        oposite = {"(": ")", "[":"]", "{":"}"}
        for index in range(len(s)):
            if s[index] in ["(", "[", "{"]:
                expecting.append(oposite[s[index]])
                continue
            if expecting == [] or expecting[-1] != s[index]:
                return False
            expecting.pop(-1)
        if len(expecting) == 0:
            return True
        return False
assert Solution().isValid("()")
assert Solution().isValid("()[]{}")
assert Solution().isValid("(]") == False
assert Solution().isValid("([)]") == False
assert Solution().isValid("{[]}")
assert Solution().isValid("([])")
assert Solution().isValid("(") == False

