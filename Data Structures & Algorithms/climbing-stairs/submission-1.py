class Solution:
    def climbStairs(self, n: int) -> int:
        def stairs(i):
            if i > n:
                return 0
            if i == n:
                return 1
            return stairs(i+1) + stairs(i+2)
        return stairs(0)    

        