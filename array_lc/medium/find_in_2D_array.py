"""剑指 Offer 04. 二维数组中的查找

在一个 n * m 的二维数组中,每一行都按照从左到右递增的顺序排序,
每一列都按照从上到下递增的顺序排序。请完成一个高效的函数,输入这样的一个二维数组和一个整数,
判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5,返回 true。

给定 target = 20,返回 false。

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
        i = 0
        j = len(matrix[0]) - 1

        while i < len(matrix) and j >= 0:
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
        i = len(matrix) - 1
        j = 0

        while i >= 0 and j < len(matrix[0]):
            data = matrix[i][j]
            if target == data:
                return True
            elif target > data:
                j += 1
            else:
                i -= 1
        return False

    def findNumberIn2DArray_official(
        self, matrix: List[List[int]], target: int
    ) -> bool:
        """官方题解及语言描述

        算法流程:
            从矩阵 matrix 左下角元素(索引设为 (i, j) )开始遍历,并与目标值对比:
                1. 当 matrix[i][j] > target 时,执行 i-- ,即消去第 i 行元素;
                2. 当 matrix[i][j] < target 时,执行 j++ ,即消去第 j 列元素;
                3. 当 matrix[i][j] = target 时,返回 true ,代表找到目标值。
            若行索引或列索引越界,则代表矩阵中无目标值,返回 false。
            每轮 i 或 j 移动后,相当于生成了“消去一行(列)的新矩阵”, 索引(i,j)
            指向新矩阵的左下角元素(标志数),因此可重复使用以上性质消去行(列)。

            复杂度分析:
                时间复杂度 O(M+N) :其中,N 和 M 分别为矩阵行数和列数,此算法最多循环 M+N 次。
                空间复杂度 O(1) : i, j 指针使用常数大小额外空间。

            作者:jyd
            链接:https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solution/mian-shi-ti-04-er-wei-shu-zu-zhong-de-cha-zhao-zuo/
            来源:力扣(LeetCode)
            著作权归作者所有。商业转载请联系作者获得授权,非商业转载请注明出处。
        """
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False
