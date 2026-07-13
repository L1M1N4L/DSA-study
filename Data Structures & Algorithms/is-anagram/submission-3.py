class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seens, seent = {}, {}
        
        for i in range(len(s)):
            if s[i] not in seens:
                seens[s[i]] = 0
            seens[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in seent:
                seent[t[i]] = 0
            seent[t[i]] += 1
        
        return seens == seent

        
        
