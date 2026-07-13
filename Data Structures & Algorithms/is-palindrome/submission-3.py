class Solution:
    def isPalindrome(self, s: str) -> bool:
        strbuild = ""
        for char in s:
            if char.isalnum():
                strbuild += char.lower()
        

        e = len(strbuild) - 1
        for i in range(len(strbuild)):
            if e <= i:
                return True
            if strbuild[e] != strbuild[i]:
                return False
            e -= 1
        return True


        