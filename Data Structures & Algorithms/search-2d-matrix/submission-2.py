class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # given a matrix, each row is in increasing order
        # the next row is also in increasing order

        rows, cols = len(matrix), len(matrix[0])
        top = 0
        bottom = rows - 1

        while top <= bottom:

            mid = (top + bottom) // 2
            # if it is greater than largest value in the row
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break

        curr_row = (top + bottom) // 2
        low = 0
        high = cols - 1

        while low <= high:
            curr_mid = (low + high) // 2
            if target == matrix[curr_row][curr_mid]:
                return True
            elif target > matrix[curr_row][curr_mid]:
                low = curr_mid + 1
            else:
                high = curr_mid - 1
        return False


