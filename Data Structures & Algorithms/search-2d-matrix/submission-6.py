class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while r > l:
            mid = l + ((r - l) // 2)

            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][0] < target:
                if matrix[mid+1] and matrix[mid+1][0] > target:
                    l = mid
                    r = mid
                else:
                    l = mid + 1
            else:
                return True
        idx = l
        r = len(matrix[idx]) - 1
        l = 0

        while r > l:
            mid = l + ((r - l) // 2)

            if matrix[idx][mid] > target:
                r = mid - 1
            elif matrix[idx][mid] < target:
                l = mid + 1
            else:
                return True
        if l == r and matrix[idx][r] == target:
            return True
        return False