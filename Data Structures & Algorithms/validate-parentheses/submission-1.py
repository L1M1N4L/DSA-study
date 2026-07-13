class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoopenmap = {"}" : "{", 
        ")":"(", 
        "]":"["}
        
        for c in s:
            if c in closetoopenmap:
                if stack and stack[-1] == closetoopenmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
