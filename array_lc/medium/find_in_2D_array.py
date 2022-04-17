"""
"""

from typing import List


class FindIn2DArray:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        """40 ms	19.2 MB
        从右上角往左下角遍历

        初始化, i = 0  j = len(matrix[0]) - 1
            1. 若 target == matrix[i][j], 则返回 True
            2. 若 target > matrix[i][j], e.g. 30 > 20
                根据题目规则, 则纵向 从上到下查找, i + 1
            3. 若 target < matrix[i][j] e.g. 20 < 30
                根据题目规则, 则横向, 从右到左查找, j - 1
        """

        row = len(matrix)
        if row == 0:
            return False

        column = len(matrix[0])
        if column == 0:
            return False

        i = 0
        j = column - 1

        while i < row and j >= 0:
            data = matrix[i][j]
            if target == data:
                return True
            elif target > data:
                i += 1
            else:
                j -= 1
        return False

    def findNumberIn2DArray_v2(self, matrix: List[List[int]], target: int) -> bool:
        """40 ms	19.2 MB
        从左下角往右上角遍历

        初始化, i = len(matrix) -1 ,j = 0
            1. 若 target == matrix[i][j], 则返回 True
            2. 若 target > matrix[i][j], e.g. 30 > 20
                根据题目规则, 则横向, 从左到右查找, j + 1
            3. 若 target < matrix[i][j] e.g. 20 < 30
                根据题目规则, 则纵向, 从下到上查找, i - 1
        """

        row = len(matrix)
        if row == 0:
            return False

        column = len(matrix[0])
        if column == 0:
            return False

        i = len(matrix) - 1
        j = 0

        while i >= 0 and j < column:
            data = matrix[i][j]
            if target == data:
                return True
            elif target > data:
                j += 1
            else:
                i -= 1
        return False
        