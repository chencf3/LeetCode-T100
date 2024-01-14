'''
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

示例 1：
输入：nums = [10,2]
输出："210"

示例 2：
输入：nums = [3,30,34,5,9]
输出："9534330"

提示：
1 <= nums.length <= 100
0 <= nums[i] <= 10^9
'''


### 方法一：手写快速排序
# 时间复杂度：O(n log n)
# 空间复杂度：O(n)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def quickSort(nums):
            if len(nums) <= 1:
                return nums
            pivot = nums[len(nums) // 2]
            left = [num for num in nums if num + pivot > pivot + num]
            mid = [num for num in nums if num + pivot == pivot + num]
            right = [num for num in nums if num + pivot < pivot + num]
            return quickSort(left) + mid + quickSort(right)

        nums = [str(num) for num in nums]
        res = ''.join(quickSort(nums))
        if res[0] == '0':
            return '0'
        return res