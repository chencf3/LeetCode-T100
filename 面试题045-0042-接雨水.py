'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9

提示：
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
'''


### 方法一：双指针
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        left_height, right_height = 0, 0
        while left <= right:
            left_height = max(left_height, height[left])
            right_height = max(right_height, height[right])
            if left_height <= right_height:
                res += left_height - height[left]
                left += 1
            else:
                res += right_height - height[right]
                right -= 1
        return res