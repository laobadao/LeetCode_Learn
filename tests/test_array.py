"""Unit test

Authors
    * JJZHAO 2022
"""


def test_RepeatedNumbersInArrays():
    from array_lc.easy.offer_03 import RepeatedNumbersInArrays

    num = RepeatedNumbersInArrays().findRepeatNumber(nums=[i for i in range(10000)] + [0])

    assert num == 0

    num = RepeatedNumbersInArrays().findRepeatNumber_v2(nums=[3, 4, 2, 0, 0, 1])

    assert num == 0