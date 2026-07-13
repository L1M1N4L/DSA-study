class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = sorted(nums)

        current = 1
        longest = 0
        if not nums:
            return 0
        for i in range(1,len(a)):
            if a[i-1] == a[i]:
                continue
            elif a[i] == a[i-1] + 1:
                current +=1
            else:
                if current > longest:
                    longest = current
                current = 1
        if current > longest:
            longest = current
        return longest
                