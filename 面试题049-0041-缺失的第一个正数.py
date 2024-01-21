'''
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

示例 1：
输入：nums = [1,2,0]
输出：3

示例 2：
输入：nums = [3,4,-1,1]
输出：2

示例 3：
输入：nums = [7,8,9,11,12]
输出：1

提示：
1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1
'''


### 方法一：
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [0] + nums
        n = len(nums)
        i = 1
        while i < n:
            while nums[i] != i and 0 < nums[i] < n and nums[i] != nums[nums[i]]:
                x = nums[i]
                nums[i], nums[x] = nums[x], nums[i]
            i += 1
        for i, x in enumerate(nums):
            if x != i:
                return i
        return n