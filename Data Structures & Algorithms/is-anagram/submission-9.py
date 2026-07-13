class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we are given 2 input strings and we need to check and return a boolean
        # on whether it has the same letters/characters as the other
        # it is said that in the constraints that s and t only consist of lowercase english letters
        
        # a naive approach to this will be sorting
        # sorting would sort everything alphabetically and we can compare
        # if both strings have the same value
        # time complexity on this costs around o (2(n log n) )


        # however, we are able to optimise this even further by using counting
        # we can make a tally on a hash map on what characters is in the strings
        # and we can compare those this is a really good idea because we basically can compare
        # it with almost constant time and traversing the arrays are basically o(s + t) or o (2n)
        
        # the approach above is already optimised and has the lowest bounded time since eventually
        # we need to traverse both of the strings to know
        # whats bad about it is the space complexity of o(n)
        # if there is no constraints it would be perfect
        # but it says that its only english alphabet lowercase characters
        # we can instead build a 26 letter arrays of 0
        # add the order of the character to the array index and then we can traverse
        # the other array and subtract from character order index

        #base case
        if len(s) != len(t):
            return False
        # initialise the array 
        
        seen = [0] * 26

        # traverse s
        for i in s:
            index = ord(i) - ord('a') 
            seen[index] += 1 
        # traverse t
        for i in t:
            index = ord(i) - ord('a') 
            seen[index] -=1 
        
        return seen == [0] * 26 
        