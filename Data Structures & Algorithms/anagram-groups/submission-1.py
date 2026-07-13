class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for i in strs:
            arrseen = [0]*26
            for j in i:
                arrseen[ord(j) - ord('a')] += 1
            seen[tuple(arrseen)].append(i)
        return list(seen.values())


