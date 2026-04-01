class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        li = 0
        lj = 0
        hi = len(matrix) - 1
        hj = len(matrix[0]) - 1
        midx = -1
        while hi >= li:
            midi = (hi + li) // 2
            if matrix[midi][0] <= target and matrix[midi][hj] >= target:
                midx = midi
                break
            elif matrix[midi][0] >= target:
                hi = midi - 1
            elif matrix[midi][hj] <= target:
                li = midi + 1
        if midx == -1:
            return False

        while hj >= lj:
            midj = (hj + lj) // 2
            if matrix[midx][midj] == target:
                return True
            elif matrix[midx][midj] >= target:
                hj = midj - 1
            else:
                lj = midj + 1
        return False
        