'''
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值 。

示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

示例 2：
输入：nums = [1], k = 1
输出：[1]

提示：
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
'''


### 方法一：维护一个递减列表 ls_value
# 时间复杂度：O(n log k)
# 空间复杂度：O(k)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        def binary(ls_value, target):
            # 寻找递减列表 ls_value 中第一个小于等于 target 的位置
            if ls_value[0] <= target:
                return 0
            if ls_value[-1] > target:
                return len(ls_value)
            left, right = 0, len(ls_value)
            while left < right:
                mid = left + (right - left) // 2
                if ls_value[mid] > target:
                    left = mid + 1
                else:
                    right = mid
            return left

        n = len(nums)
        res = []
        ls_value = [nums[0]]
        ls_index = [0]
        for i in range(1, n):
            if i - ls_index[0] >= k:  # 只有第一个元素可能需要删除
                del ls_value[0]
                del ls_index[0]
            loc = binary(ls_value, nums[i])
            del ls_value[loc:]
            del ls_index[loc:]
            ls_value.append(nums[i])
            ls_index.append(i)
            if i >= k - 1:
                res.append(ls_value[0])
        return res


### 方法二：维护一个大小为 k 的最小堆
# 时间复杂度：O(n log n)
# 空间复杂度：O(k)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(heap)
        res = [-heap[0][0]]

        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while i - heap[0][1] >= k:
                heapq.heappop(heap)
            res.append(-heap[0][0])

        return res