"""Unit test

Authors
    * JJZHAO 2022
"""


def test_():
    from string_lc.easy.replace_space import Solution

    replaced_s = Solution().replaceSpace_v2("We are happy.")

    assert replaced_s == r"We%20are%20happy."