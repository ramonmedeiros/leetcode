class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        h = len(haystack)
        if n == 0 and h == 0:
            return 0

        if n == 0:
            return 0

        for index in range(h):
            if haystack[index] == needle[0] and n <= h-index:
                for index2 in range(1, n):
                    if haystack[index+index2] != needle[index2]:
                        break
                else:
                    return index
                continue
        return -1
assert Solution().strStr(haystack = "hello", needle = "ll") == 2
assert Solution().strStr(haystack = "aaaaa", needle = "bba") == -1
assert Solution().strStr(haystack = "mississippi", needle = "issip") == 4
