class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for _ in range(len(nums)+1)]

        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 0
            count[nums[i]] += 1
        
        for n , c in count.items():
            bucket[c].append(n)

        res = []
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res

        


