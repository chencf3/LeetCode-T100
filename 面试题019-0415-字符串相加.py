'''
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。

示例 1：
输入：num1 = "11", num2 = "123"
输出："134"

示例 2：
输入：num1 = "456", num2 = "77"
输出："533"

示例 3：
输入：num1 = "0", num2 = "0"
输出："0"

提示：
1 <= num1.length, num2.length <= 10^4
num1 和num2 都只包含数字 0-9
num1 和num2 都不包含任何前导零
'''


### 方法一：
# 时间复杂度：O(max(m, n))
# 空间复杂度：O(1)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        if m > n:
            return self.addStrings(num2, num1)

        res = ''
        num1, num2, flag = num1[::-1], num2[::-1], 0
        for i in range(n):
            if i < m:
                tmp = int(num1[i]) + int(num2[i]) + flag
            else:
                tmp = int(num2[i]) + flag
            flag = 1 if tmp // 10 == 1 else 0
            res = str(tmp % 10) + res

        return '1' + res if flag == 1 else res