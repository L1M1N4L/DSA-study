class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sett = set(nums)
        max_count = 1
        for i in nums:
            if i - 1 not in sett:
                current = i
                count = 1
                while current + 1 in sett:
                    current += 1
                    count += 1
                max_count = max(count,max_count)

        return max_count
