class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        lofcharacter = {")":"(","]":"[","}":"{"}

        for char in s:
            if char in lofcharacter:
                if seen and seen[-1] in lofcharacter[char]:
                    seen.pop()
                else: 
                    return False
            else:
                seen.append(char)
        return True if not seen else False
