'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例 2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1

提示：
你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
'''


### 方法一：调api二分查找
# 时间复杂度：O(log n)
# 空间复杂度：O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = bisect_left(nums, target)
        if res < len(nums) and nums[res] == target:
            return res
        return -1


### 方法二：手写二分查找，左闭右开写法
# 时间复杂度：O(log n)
# 空间复杂度：O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return -1