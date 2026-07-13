class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 0
            counter[i] += 1

        counts = []
        for i , j in counter.items():
            counts.append([i , j])
        meow = sorted(counts , key = lambda x : x[1], reverse=True)
        res = []
        
        for i in meow:
            res.append(i[0])
        return res[:k]
            
        