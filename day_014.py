"""
Implement a function to check if a linked list is a palindrome.

 

Example 1:

Input:  1->2
Output:  false
Example 2:

Input:  1->2->2->1
Output:  true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list-lcci
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        copy = head
        while head:
            stack.append(head.val)
            head = head.next

        while copy:
            if not copy.val == stack.pop():
                return False

            copy = copy.next

        return True
