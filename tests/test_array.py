"""Unit test

Authors
    * JJZHAO 2022
"""


def test_RepeatedNumbersInArrays():
    from array_lc.easy.repeated_numbers import RepeatedNumbersInArrays

    num = RepeatedNumbersInArrays().findRepeatNumber(
        nums=[i for i in range(10000)] + [0]
    )

    assert num == 0

    num = RepeatedNumbersInArrays().findRepeatNumber_v2(nums=[3, 4, 2, 0, 0, 1])

    assert num == 0


def test_FindIn2DArray():
    from array_lc.medium.find_in_2D_array import FindIn2DArray

    matirx = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]

    ret = FindIn2DArray().findNumberIn2DArray(matrix=matirx, target=30)

    assert ret

    ret = FindIn2DArray().findNumberIn2DArray(matrix=matirx, target=20)

    assert not ret

    ret = FindIn2DArray().findNumberIn2DArray(matrix=[[5], [6]], target=4)

    assert not ret

    ret = FindIn2DArray().findNumberIn2DArray(matrix=[[-1], [-1]], target=-2)

    assert not ret

    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    ret = FindIn2DArray().findNumberIn2DArray(matrix=matrix, target=15)

    assert ret

    ret = FindIn2DArray().findNumberIn2DArray(matrix=[[1, 3, 5]], target=5)

    assert ret

    ret = FindIn2DArray().findNumberIn2DArray(matrix=[[1], [3], [5]], target=5)

    assert ret
