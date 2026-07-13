class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num , counts in count.items():
            bucket[counts].append(num)
        

        res = 0
        for i in range(len(bucket) - 1 , 0 , -1):
            if bucket[i]:
                res = bucket[i][0]
                return res


        