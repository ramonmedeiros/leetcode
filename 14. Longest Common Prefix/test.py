class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 2:
            return "".join(strs)
        pref = self.prefix(strs[0], strs[1])
        if len(strs) == 2:
            return pref
        
        for i in range(2,len(strs)):
            pref = self.prefix(pref, strs[i])
        return pref
    
    def prefix(self, str1, str2):
        l = len(str1)
        l2 = len(str2)
        le = l
        if l2 < l:
            le = l2
        i = -1
        for i in range(le):
            if str1[i] == str2[i]:
                continue
            i = i - 1
            break
        return str1[:i+1]
assert Solution().longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert Solution().longestCommonPrefix(["dog","racecar","car"]) == ""
assert Solution().longestCommonPrefix(["c", "c"]) == "c"
