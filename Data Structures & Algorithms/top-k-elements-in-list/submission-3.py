class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        count = Counter(nums)  
        
        for n , c in count.items():
            bucket[c].append(n)
    

        res = []
        for i in range(len(bucket) - 1, 0 , -1):
            for j in bucket[i]:
                if bucket[i]:
                    res.append(j)
            if len(res) == k:
                return res





        