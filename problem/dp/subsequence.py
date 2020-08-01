"""
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。字符串 t 可能会很长.
#  示例 1:
# s = "abc", t = "ahbgdc"
#
#  返回 true.
#
#  示例 2:
# s = "axc", t = "ahbgdc"
#
#  返回 false.
#
def isSubsequence(self, s, t):
"""


def is_subsequence_by_two_pointer(s, t):
    i, j = 0, 0
    while (i < len(s) and j < len(t)):
        if s[i] == t[j]:
            i += 1

        j += 1

    return i == len(s)


if __name__ == '__main__':
    print(is_subsequence_by_two_pointer("axc", "ahbgdc"))
    print(is_subsequence_by_two_pointer("abc", "ahbgdc"))
