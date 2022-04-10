"""Unit test

Authors
    * JJZHAO 2022
"""

def test_RepeatedNumbersInArrays():
    from array_leetcode.easy.offer_03 import RepeatedNumbersInArrays

    num = RepeatedNumbersInArrays().findRepeatNumber(nums=[2, 3, 4, 5, 6, 2])
    
    assert num == 2