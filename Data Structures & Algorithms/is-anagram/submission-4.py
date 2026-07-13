class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countc = {}
        count = {}
        for c in s:
            if c not in countc:
                countc[c] = 1
            countc[c] += 1
        
        for m in t:
            if m not in count:
                count[m] = 1
            count[m] += 1

        return countc == count

        