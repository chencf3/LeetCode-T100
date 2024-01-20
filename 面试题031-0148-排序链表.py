'''
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例 3：
输入：head = []
输出：[]

提示：
链表中节点的数目在范围 [0, 5 * 10^4] 内
-10^5 <= Node.val <= 10^5

进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
'''


### 方法一：归并排序
# 时间复杂度：O(n log n)
# 空间复杂度：O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            cur = dummy = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    cur = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    cur = list2
                    list2 = list2.next
            if list1 is None:
                cur.next = list2
            if list2 is None:
                cur.next = list1
            return dummy.next
        
        dummy = ListNode(next=head)
        n = 0  # 链表长度
        cur = head
        while cur:
            cur = cur.next
            n += 1

        k = 1  # 子链表长度从 k=1 开始，翻倍增长
        while k < n:
            # 依次合并两个长度为 k 的链表
            pre, cur = dummy, dummy.next
            while cur:
                # 第1个长度为 k 的链表，头节点为left
                left = cur      
                for _ in range(k - 1):  # k-1 步
                    if cur.next:
                        cur = cur.next
                    else:  # left链表长度未达到k，提前结束
                        break
                
                if cur.next is None:
                    # 如果cur.next不存在意味着没有right，提前结束
                    pre.next = left
                    break
                
                # 第2个长度为 k 的链表，头节点为right
                right = cur.next    
                cur.next = None  # 断开left和right的链表
                cur = right
                for _ in range(k - 1):  # k-1 步
                    if cur.next:
                        cur = cur.next
                    else:  # right链表长度未达到k，提前结束
                        break
                
                # 断开right链表与后续链表
                nxt = None
                if cur.next:
                    nxt = cur.next
                    cur.next = None
                cur = nxt  # cur继续指向下一个链表

                # 合并两个排好序的链表
                merged = mergeTwoLists(left, right)
                pre.next = merged
                while pre.next:
                    pre = pre.next  # 移动到当前排序好的链表尾部

            k *= 2  # 子链表长度翻倍
        
        return dummy.next