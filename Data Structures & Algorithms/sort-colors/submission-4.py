class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0 , 0 , 0]

        for i in nums:
            bucket[i] += 1
        
        k = 0
        for i in range(len(bucket)):
            for _ in range(bucket[i]):
                nums[k] = i
                k += 1
