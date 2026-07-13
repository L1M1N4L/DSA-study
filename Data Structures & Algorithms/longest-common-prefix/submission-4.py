class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        currlongestpref = ""
        
        for i in range(len(strs[0])):
            for j in strs:
                if len(j) <= i:
                    return currlongestpref
                if j[i] != strs[0][i]:
                    return currlongestpref
            
            currlongestpref += strs[0][i]
        return currlongestpref