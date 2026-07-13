class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0] * 3    
        for i in nums:
            bucket[i] += 1

        for i in range(len(nums)):
            nums.pop()
        
        for i in range(len(bucket)):
            for j in range(bucket[i]):
                nums.append(i)
        return nums