class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maap = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for c in s:
            if c in maap:
                if stack and stack[-1] == maap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False