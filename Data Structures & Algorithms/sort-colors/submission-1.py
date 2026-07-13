class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hm = {0: 0, 1: 0, 2: 0}  
        
        for i in nums:
            hm[i] += 1
        
        idx = 0
        for color in [0, 1, 2]:
            for _ in range(hm[color]):
                nums[idx] = color
                idx += 1