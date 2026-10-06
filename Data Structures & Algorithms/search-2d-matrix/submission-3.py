class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # start with t, b pointers
        # if target > t[0] and target < b[-1], we found its row, run binary search
        # else if target < mid[0], move b pointer up
        # else if target > mid[-1], move t pointer down
        t, b = 0, len(matrix) - 1
        while t <= b:
            mid = (t + b) // 2
            if target < matrix[mid][0]:
                b = mid - 1
            elif target > matrix[mid][-1]:
                t = mid + 1
            else:
                break
        
        if t > b:
            return False
        
        l, r = 0, len(matrix[mid]) - 1
        while l <= r:
            mid_index = (l + r) // 2
            if target > matrix[mid][mid_index]:
                l = mid_index + 1
            elif target < matrix[mid][mid_index]:
                r = mid_index - 1
            else:
                return True

        return False
