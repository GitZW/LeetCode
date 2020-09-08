# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。 
# 
#  示例： 
# 
#  给定一个链表: 1->2->3->4->5, 和 n = 2.
# 
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#  
# 
#  说明： 
# 
#  给定的 n 保证是有效的。 
# 
#  进阶： 
# 
#  你能尝试使用一趟扫描实现吗？ 
#  Related Topics 链表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first_pointer = last_pointer = head
        for i in range(n):
            first_pointer = first_pointer.next
        if not first_pointer:
            # 删除第一个节点
            return last_pointer.next

        while first_pointer.next:
            first_pointer = first_pointer.next
            last_pointer = last_pointer.next
        last_pointer.next = last_pointer.next.next

        return head

