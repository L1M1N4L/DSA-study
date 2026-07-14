class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
                
            left_array = nums[:len(nums)//2]
            right_array = nums[len(nums)//2:]

            self.sortArray(left_array)
            self.sortArray(right_array)


            l = 0
            r = 0
            k = 0

            while l < len(left_array) and r < len(right_array):
                if left_array[l] < right_array[r]:
                    nums[k] = left_array[l]
                    l += 1
                else:
                    nums[k] = right_array[r]
                    r += 1

                k += 1

            while l < len(left_array):
                nums[k] = left_array[l]
                l += 1
                k += 1

            while r < len(right_array):
                nums[k] = right_array[r]
                r += 1
                k += 1      
        return nums


        