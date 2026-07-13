class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        freq = []
        
        for i in range(len(nums) + 1):
            freq.append([])

        for key , v in count.items():
            freq[v].append(key)
        res = []
        for i in range(len(freq) - 1, -1 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
