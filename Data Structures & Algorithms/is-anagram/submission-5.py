class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0]*26
        for c in s:
            arrnum = ord(c) - ord("a") 
            arr[arrnum] += 1

        for c in t:
            arrnum = ord(c) - ord("a")
            arr[arrnum] -= 1
        
        return arr == [0]*26
