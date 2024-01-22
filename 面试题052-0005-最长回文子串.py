'''
给你一个字符串 s，找到 s 中最长的回文子串。
如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"

提示：
1 <= s.length <= 1000
s 仅由数字和英文字母组成
'''


### 方法一：动态规划
# 时间复杂度：O(n ^ 2)
# 空间复杂度：O(n ^ 2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1):
            dp[i][i] = True
            dp[i][i + 1] = (s[i] == s[i + 1])
        dp[n - 1][n - 1] = True

        for x in range(2, n):
            for i in range(n - x):
                dp[i][i + x] = (dp[i + 1][i + x - 1] and s[i] == s[i + x])

        res, max_len = '', 0
        for i in range(n):
            for j in range(i, n):
                if dp[i][j] == True and j - i + 1 > max_len:
                    res = s[i: j + 1]
                    max_len = j - i + 1
        return res