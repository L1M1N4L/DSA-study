class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        resarr = []
        for i in range(len(nums)):
            numsdecoy = nums[:]
            mult = []
            for j in range(len(nums)):
                numsdecoy[i] = 1
                mult.append(numsdecoy[j])
            mult_in = 1
            for x in mult:
                mult_in *= x
            resarr.append(mult_in)

        return resarr
                

        