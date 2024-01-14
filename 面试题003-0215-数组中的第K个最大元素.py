'''
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1:
输入: [3,2,1,5,6,4], k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4

提示：
1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
'''


### 方法一：调api建最小堆
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
    

### 方法二：手写最小堆
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class MinHeap:
    def __init__(self):
        # 初始化一个空列表来存储堆的元素
        self.heap = []
        self.size = 0

    # 获取父节点索引  
    def parent(self, i):
        return (i - 1) // 2

    # 获取左子节点索引
    def left(self, i):
        return 2 * i + 1

    # 获取右子节点索引
    def right(self, i):
        return 2 * i + 2

    # 交换两个元素的位置
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # 上浮操作，将节点i与其父节点进行比较，如果节点i的值小于父节点的值，则交换它们的位置
    def sift_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    # 下沉操作，将节点i与其左右子节点进行比较，如果节点i的值大于其子节点的值，则交换它们的位置，并继续下沉操作
    def sift_down(self, i):
        while self.left(i) < self.size:  # 有left左节点时即可下沉
            min_child = self.left(i)
            if self.right(i) < self.size and self.heap[self.right(i)] < self.heap[self.left(i)]:
                min_child = self.right(i)
            if self.heap[i] <= self.heap[min_child]:
                break
            self.swap(i, min_child)
            i = min_child

    # 向堆中插入一个元素，并保持堆的性质不变
    def push(self, item):
        self.size += 1
        self.heap.append(item)
        self.sift_up(self.size - 1)

    # 从堆中删除最小元素（根节点），并保持堆的性质不变
    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        min_val = self.heap[0]  # 保存最小元素的值
        self.heap[0] = self.heap[-1]  # 将最后一个元素替换为根节点元素
        del self.heap[-1]  # 删除最后一个元素
        self.sift_down(0)  # 对根节点进行下沉操作，保持堆的性质不变
        return min_val  # 返回最小元素的值

    # 获取最小元素（根节点）
    def peak(self):
        return self.heap[0]
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MinHeap()
        for num in nums:
            heap.push(num)
            if heap.size > k:
                heap.pop()
        return heap.peak()
    

### 方法三：手写快速排序
# 时间复杂度：O(n log n)
# 空间复杂度：O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSort(nums):
            if len(nums) <= 1:
                return nums
            pivot = nums[len(nums) // 2]
            left = [num for num in nums if num < pivot]
            mid = [num for num in nums if num == pivot]
            right = [num for num in nums if num > pivot]
            return quickSort(left) + mid + quickSort(right)

        res = quickSort(nums)
        return res[-k]