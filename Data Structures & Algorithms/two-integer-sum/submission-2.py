class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # classic twosum problem given a target we need to find 2 numbers from a list of 
        # nubers nums and return their index

        # a naive approach to this is that we can add every single pair of indices and when it matches
        # the target check you can return the index for both
        # however this is time consuming which takes o(n^2) time to do so

        # a way to optimise this is to sort the array. once you sort it you can then use
        # a two pointer algorithm to use a kind of greedy algorithm till it matches the target

        # but it will still take a o(n log n + n) time
        # thus we can use a dictionary approach where we keep the seen and indices as key value pairs
        # after that we can calculate the difference and search using o(1) time thus only requires one pass

        seen = {}
        # we need to use this to keep track of the index
        for i in range(len(nums)):
            #find the difference
            difference = target - nums[i]

            # check if difference exists in hashmap
            if difference in seen:
                return [seen[difference], i]
            # not found add to value
            seen[nums[i]] = i
        return -1
            
                

            