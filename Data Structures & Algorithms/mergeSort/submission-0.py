# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List['Pair']) -> List['Pair']:
        if len(pairs) <= 1:
            return pairs

        m = len(pairs) // 2
        left = self.mergeSort(pairs[:m])
        right = self.mergeSort(pairs[m:])

        return self.merge(left, right)
        

    def merge(self, s: List['Pair'], e: List['Pair']) -> List['Pair']:
        result = []
        i, j = 0, 0
        while i < len(s) and j < len(e):
            if s[i].key <= e[j].key:
                result.append(s[i])
                i += 1
            else:
                result.append(e[j])
                j += 1

        result.extend(s[i:])
        result.extend(e[j:])

        return result
