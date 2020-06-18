"""
Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty. When the stack is empty, peek should return -1.

Example1:

 Input:
["SortedStack", "push", "push", "peek", "pop", "peek"]
[[], [1], [2], [], [], []]
 Output:
[null,null,null,1,null,2]
Example2:

 Input:
["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]
[[], [], [], [1], [], []]
 Output:
[null,null,null,null,null,true]
Note:

The total number of elements in the stack is within the range [0, 5000].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-of-stacks-lcci
"""


class SortedStack:

    def __init__(self):
        self.sorted_stack = []

    def push(self, val: int) -> None:
        help_stack = []

        while self.sorted_stack and val > self.sorted_stack[-1]:
            help_stack.append(self.pop())
        self.sorted_stack.append(val)
        while help_stack:
            self.sorted_stack.append(help_stack.pop())

    def pop(self) -> None:
        if self.isEmpty():
            return None
        return self.sorted_stack.pop()

    def peek(self) -> int:
        if self.isEmpty():
            return -1

        return self.sorted_stack[-1]

    def isEmpty(self) -> bool:
        return len(self.sorted_stack) == 0

# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
