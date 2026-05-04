class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_r = len(matrix)
        n_c = len(matrix[0])

        l_r, r_r = 0, n_r - 1
        l_c, r_c = 0, n_c - 1

        mid_r = l_r + ((r_r - l_r) // 2)
        mid_c = l_c + ((r_c - l_c) // 2)

        while l_r < r_r:
            if matrix[mid_r][-1] == target:
                return True
            elif matrix[mid_r][-1] > target:
                r_r = mid_r
            else:
                l_r = mid_r + 1
            mid_r = l_r + ((r_r - l_r) // 2)


        while l_c <= r_c:
            if matrix[mid_r][mid_c] == target:
                return True
            elif matrix[mid_r][mid_c] > target:
                r_c = mid_c - 1
            else:
                l_c = mid_c + 1
            mid_c = l_c + ((r_c - l_c) // 2)

        return False

