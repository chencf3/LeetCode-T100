'''
给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。

示例 1：
输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
输出：3
解释：长度最长的公共子数组是 [3,2,1] 。

示例 2：
输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
输出：5

提示：
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
'''


### 方法一：动态规划
# 时间复杂度：O(n * m)
# 空间复杂度：O(n * m)
'''
状态定义：dp[i, j] 表示 nums1[:i]中以i结尾的子数组 和 nums2[:j]中以j结尾的子数组 的重复子数组长度
状态转移方程：
(1) 若 nums1[i] == nums2[j]，dp[i][j] = dp[i - 1][j - 1] + 1
(2) 若 nums1[i] != nums2[j]，dp[i][j] = 0
'''
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
        return max([max(row) for row in dp])