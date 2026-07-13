class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colorcount = [0 , 0 , 0]
        
        for n in nums:
            colorcount[n] += 1
        
        i = 0
        for n in range(len(colorcount)):
            for j in range(colorcount[n]):
                nums[i] = n
                i += 1
        return