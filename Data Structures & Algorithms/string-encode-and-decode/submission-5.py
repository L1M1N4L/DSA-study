class Solution:

    def encode(self, strs: List[str]) -> str:
        string_builder = ''
        for i in strs:
            string_builder += str(len(i)) + '#' + i 
        return string_builder

    def decode(self, s: str) -> List[str]:
        res = []
        j = 0
        if s == '':
            return []
        while j < len(s):
            i = j
            while s[i] != '#':
                i += 1
            noOfChar = int(s[j:i])
            res.append(str(s[i + 1 : i + 1 + noOfChar]))
            j = i + 1 + noOfChar
        return res


            
            
    
