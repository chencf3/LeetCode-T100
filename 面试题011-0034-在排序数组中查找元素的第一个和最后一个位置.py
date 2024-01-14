'''
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]

提示：
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums 是一个非递减数组
-10^9 <= target <= 10^9
'''


### 方法一：调api二分查找
# 时间复杂度：O(log n)
# 空间复杂度：O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = bisect_left(nums, target)
        if left == n or nums[left] != target:
            return [-1, -1]
        return [left, bisect_right(nums, target) - 1]


### 方法二：手写二分查找，左闭右开写法
# 时间复杂度：O(log n)
# 空间复杂度：O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        n = len(nums)
        left = lower_bound(nums, target)
        if left == n or nums[left] != target:
            return [-1, -1]
        return [left, lower_bound(nums, target + 1) - 1]