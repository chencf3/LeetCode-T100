'''
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
整数除法仅保留整数部分。
你可以假设给定的表达式总是有效的。所有中间结果将在 [-2^31, 2^31 - 1] 的范围内。
注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。

示例 1：
输入：s = "3+2*2"
输出：7

示例 2：
输入：s = " 3/2 "
输出：1

示例 3：
输入：s = " 3+5 / 2 "
输出：5

提示：
1 <= s.length <= 3 * 10^5
s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
s 表示一个 有效表达式
表达式中的所有整数都是非负整数，且在范围 [0, 2^31 - 1] 内
题目数据保证答案是一个 32-bit 整数
'''


### 方法一：栈
# 时间复杂度：O(n)
# 空间复杂度：O(n)
'''
加减时入栈，乘除时出栈，计算后再入栈
'''
class Solution:
    def calculate(self, s: str) -> int:
        s = ''.join([c for c in s if c != ' '])
        n = len(s)
        symbol = '+'
        stack, left = [], 0
        for right in range(1, n + 1):
            if right == n or s[right] in '+-*/':
                num = int(s[left: right])
                if symbol == '+':
                    stack.append(num)
                elif symbol == '-':
                    stack.append(-num)
                elif symbol == '*':
                    stack.append(stack.pop() * num)
                else:
                    x = stack.pop()
                    if x >= 0:
                        stack.append(x // num)
                    else:
                        stack.append(-((-x) // num))
                if right < n:
                    symbol = s[right]
                left = right + 1
        return sum(stack)