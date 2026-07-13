class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        arr = []
        for i , j in freq.items():
            arr.append([j , i])
        arr.sort(reverse=True)

        result = []
        for i in range(k):
            result.append(arr[i][1])
        return result

        


