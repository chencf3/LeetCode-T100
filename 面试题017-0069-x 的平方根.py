'''
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

示例 1：
输入：x = 4
输出：2

示例 2：
输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。

提示：
0 <= x <= 2^31 - 1
'''


### 方法一：二分，左闭右开写法
# 时间复杂度：O(log n)
# 空间复杂度：O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        # 返回满足 k ** 2 <= x 的最大整数 k
        if x <= 1:
            return x
        
        def lower_bound(x):
            # 返回满足 k ** 2 >= x 的最小整数 k
            left, right = 0, x // 2 + 1
            while left < right:
                mid = left + (right - left) // 2
                if mid * mid == x:
                    return mid
                elif mid * mid > x:
                    right = mid
                else:
                    left = mid + 1
            return left

        return lower_bound(x + 1) - 1