class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        scount = {}
        tcount = {}

        for c in s:
            if c not in scount:
                scount[c] = 0
            scount[c] += 1
        
        for c in t:
            if c not in tcount:
                tcount[c] = 0
            tcount[c] += 1    
        
        return scount == tcount
