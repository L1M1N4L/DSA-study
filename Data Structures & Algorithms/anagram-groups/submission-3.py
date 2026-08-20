class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for i in strs:
            freq = [0] * 26
            
            for c in i:
                freq[ord(c) - ord('a')] += 1
            
            if str(freq) not in seen:
                seen[str(freq)] = []
            seen[str(freq)].append(i)
        
        return list(seen.values())
