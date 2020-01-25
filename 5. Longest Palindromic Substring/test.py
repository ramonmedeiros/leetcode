class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        biggest = ""
        for i in range(len(s)-1):
            # odd palindrome
            a = self.checkPalindrome(s, i, i)
            b = self.checkPalindrome(s, i, i+1)
            bigger = a
            if len(b) > len(a):
                bigger = b
            if len(bigger) > len(biggest):
                biggest = bigger
        return biggest

    def checkPalindrome(self, string: str, beg:int , end:int):
        while beg > 0 and end < len(string) and string[beg] == string[end]:
                beg = beg - 1
                end = end + 1
        return string[beg:end+1]
print(Solution().longestPalindrome("babad"))
