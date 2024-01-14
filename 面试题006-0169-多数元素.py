'''
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：
输入：nums = [3,2,3]
输出：3

示例 2：
输入：nums = [2,2,1,1,1,2,2]
输出：2

提示：
n == nums.length
1 <= n <= 5 * 104
-10^9 <= nums[i] <= 10^9

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
'''


### 方法一：调用api统计元素个数
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return cnt.most_common(1)[0][0]
    

### 方法二：手动统计元素个数
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = len(nums) // 2
        cnt = dict()
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1
        for k in cnt:
            if cnt[k] > m:
                return k
            
    
### 方法三：摩尔投票法，票数正负抵消
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0:
                res = num
            if num == res:
                votes += 1
            else:
                votes -= 1
        return res