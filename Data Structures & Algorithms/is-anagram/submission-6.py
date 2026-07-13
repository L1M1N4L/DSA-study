class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we need to return true such that all the letters in s would be equal to the letters in t
        # first we can try sorting the s and t string amd see if it matches
        # then return the sorted value
        # however its not efficient enough because it will take o(n log n) in every sort with a new string since strings are immutable in python. thus taking more space
        # a clever solution for this, is that since we only need to know the number of words we can tally it using some sort of hashmap.
        # and we can compare both hashmap together and return true if the hashmapis the same ths will only take o(s + t)
        # however we can further optimize it by using some sort of array because it only gives us lowercase english letters.
        # thus we can use an array of 1 and 0s to scan through all the input in s and increase the count on the 25 positions of the array
        # and we can decrase the copunt on t this will also take the same time however a constant space will remain.

        if len(s) != len(t):
            return False
        
        array = [0]*26

        for i in s:
            index = ord(i) - ord('a')
            array[index] += 1
        for i in t:
            index = ord(i) - ord('a')
            array[index] -= 1

        return array == [0]*26
        