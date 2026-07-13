class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        editarr = [0] * 26
        if len(s) != len(t):
            return False

        for c in s:
            editarr[ord(c) - ord('a')] += 1

        for c in t:
            editarr[ord(c) - ord('a')] -= 1
        
        return editarr == [0] * 26