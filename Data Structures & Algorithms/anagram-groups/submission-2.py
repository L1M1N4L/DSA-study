class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        
        for i in strs:
            seen = [0] * 26
            for j in i:
                seen[ord(j) - ord('a')] += 1
            dictionary[str(seen)].append(i)
        return list(dictionary.values())


        
                