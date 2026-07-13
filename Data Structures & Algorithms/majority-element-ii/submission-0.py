class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen = {}
        res = [] 
        for i in nums:
            if i not in seen:
                seen[i] = 0
            seen[i] += 1

        for key , value in seen.items():
            if value > len(nums) // 3:
                res.append(key)
        return res        

        