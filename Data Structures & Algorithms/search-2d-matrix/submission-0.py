class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        down = len(matrix) - 1

        while up <= down:
            mid = (down + up) // 2
            if target < matrix[mid][0]:
                down = mid - 1
            elif target > matrix[mid][-1]:
                up = mid + 1
            else:
                left = 0
                right = len(matrix[mid])
                while left <= right:
                    mid2 = (right + left) // 2
                    if target < matrix[mid][mid2]:
                        right = mid2 - 1
                    elif target > matrix[mid][mid2]:
                        left = mid2 + 1
                    else:
                        return True
                return False
        return False 
        