class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        down = len(matrix) - 1
        cols = len(matrix[0])
        while up <= down:
            index = ((down - up) // 2 ) + up
            if matrix[index][0] == target:
                return True
            elif target > matrix[index][0] and target <= matrix[index][cols-1]:
                break
            elif target > matrix[index][cols-1]:
                up = index + 1
            elif target < matrix[index][0]:
                down = index - 1
        
        left = 0
        right = len(matrix[index]) - 1
        while left <= right:
            index1 = ((right- left) // 2 ) + left
            if matrix[index][index1] == target:
                return True
            elif target > matrix[index][index1]:
                left = index1 + 1
            else:
                right = index1 - 1
        return False