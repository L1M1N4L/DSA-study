class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for key , value in count.items():
            bucket[value].append(key)
        
        res = []
        
        for i in range(len(bucket) - 1 , 0 , -1):
            for j in bucket[i]:
                res.append(j)
        return res[:k]



        