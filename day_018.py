"""
How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> return -3.
minStack.pop();
minStack.top();      --> return 0.
minStack.getMin();   --> return -2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-stack-lcci
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []

    def push(self, x: int) -> None:
        self.min_stack.append(x)

    def pop(self) -> None:
        return self.min_stack.pop()

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return min(self.min_stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
