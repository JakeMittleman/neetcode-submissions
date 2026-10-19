class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def bs(l, r):
            if l > r:
                return False

            m = (l+r) // 2
            row = matrix[m]

            # target is here
            if target >= row[0] and target <= row[-1]:
                return bs2(0, COLS-1, row)

            elif target < row[0]:
                return bs(l, m-1)

            else:
                return bs(m+1, r)

        def bs2(l, r, arr):
            if l > r:
                return False

            m = (l+r) // 2
            if arr[m] == target:
                return True

            elif arr[m] < target:
                return bs2(m+1, r, arr)

            else:
                return bs2(l, m-1, arr)

        return bs(0, ROWS-1)