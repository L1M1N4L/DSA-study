class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make the counter
        counter = {}
        # we add a + 1 because there is a total of more than 0 - nums freq
        frequency = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            if i not in counter:
                counter[i] = 0
            counter[i] += 1

        for num , freq in counter.items():
            frequency[freq].append(num)
        
        res = []
        for i in range(len(frequency) - 1, 0 , -1):
            for num in frequency[i]:
                res.append(num)
        return res[:k]


