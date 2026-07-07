class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_idx = 0
        # find the row using binary search
        if len(matrix) > 1:
            left = 0
            right = len(matrix) - 1
            while left <= right:
                mid = (left + right) // 2
                
                if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                    row_idx = mid
                    break
                elif target < matrix[mid][0] and target < matrix[mid][-1]:
                    right = mid - 1
                else: left = mid + 1

        
        left = 0
        right = len(matrix[0]) - 1
        row = matrix[row_idx]
        while (left <= right):
            mid = (left + right) // 2
            if row[mid] == target: return True
            elif row[mid] > target: right = mid - 1
            else: left = mid + 1
        
        return False

        # find the target on the row using binary search 