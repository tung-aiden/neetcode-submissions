import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # given a matrix, each row is in increasing order
        # the next row is also in increasing order
        arr = np.array(matrix)
        arr = arr.flatten()
        print(arr)

        low = 0
        high = len(arr) - 1
        print(high)

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False