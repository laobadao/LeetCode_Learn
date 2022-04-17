"""剑指 Offer 05. 替换空格

请实现一个函数,把字符串 s 中的每个空格替换成"%20"。

示例 1:

输入:s = "We are happy."
输出:"We%20are%20happy."

限制:

0 <= s 的长度 <= 10000

来源:力扣(LeetCode)
链接:https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
著作权归领扣网络所有。商业转载请联系官方授权,非商业转载请注明出处。

"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        # 40 ms	15 MB
        return s.replace(" ", "%20")

    def replaceSpace_v2(self, s: str) -> str:
        # 40 ms	15 MB
        s_split = s.split(" ")
        s_replaced = s_split[0]
        for s_ in s_split[1:]:
            s_replaced = s_replaced + "%20" + s_
        return s_replaced

    def replaceSpace_v3(self, s: str) -> str:
        """32 ms	15 MB
        """
        s_list = list(s)
        s_replaced = ""
        for s_ in s_list:
            replaced_char = "%20" if s_ == " " else s_
            s_replaced = s_replaced + replaced_char
        return s_replaced
