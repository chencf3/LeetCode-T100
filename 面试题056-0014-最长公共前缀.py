'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

提示：
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成
'''


### 方法一：
# 时间复杂度：O(n * m)
# 空间复杂度：O(n)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        n = inf
        for s in strs:
            n = min(n, len(s))
        for i in range(n):
            if len(set([s[i] for s in strs])) == 1:
                res += s[i]
            else:
                break
        return res