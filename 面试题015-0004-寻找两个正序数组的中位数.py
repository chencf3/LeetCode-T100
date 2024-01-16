'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。

示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

提示：
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
'''


### 方法一：二分，左闭右开写法
# 时间复杂度：O(log min(m, n))
# 空间复杂度：O(1)
'''
若 m + n 为奇数，寻找第 (m + n + 1) // 2 小的数，
若 m + n 为偶数，寻找第 (m + n) // 2 小的数，再和比它稍大的数求平均值，
综上所述，先寻找第 (m + n + 1) // 2 小的数。

若看成在 num1 索引为 i 的数前面插一块板将 nums1 分成两部分，
在 num2 索引为 j 的数前面插一块板将 nums2 分成两部分，
那么需要满足 i + j == (m + n + 1) // 2，
要寻找的数为 num1[i - 1] 和 num2[j - 1] 中的较大值。
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        def get_value(nums, i):
            if 0 <= i < len(nums):
                return nums[i]
            elif i < 0:
                return -inf
            else:
                return inf

        k = (m + n + 1) // 2
        left, right = 0, m + 1  # 插入的板最多可以放到 num1 索引为 m 的数前面，所以在左闭右开写法中 right 初始化为 m + 1
        while left < right:
            mid = left + (right - left) // 2
            x1, x2 = get_value(nums1, mid - 1), get_value(nums1, mid)
            y1, y2 = get_value(nums2, k - mid - 1), get_value(nums2, k - mid)
            if x1 <= y2 and y1 <= x2:
                break
            elif x1 > y2:
                right = mid
            else:
                left = mid + 1

        if (m + n) % 2 == 1:
            return max(x1, y1)
        return (max(x1, y1) + min(x2, y2)) / 2