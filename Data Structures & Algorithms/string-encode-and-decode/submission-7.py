class Solution:

    def encode(self, strs: List[str]) -> str:
        
        string_builder = ''
        
        for i in strs:
            string_builder += str(len(i)) + '#' + i
        return string_builder

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i : j])
            res.append(s[j + 1: length + j + 1])
            i = length + j + 1
        return res

