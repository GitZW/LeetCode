"""
Describe how you could use a single array to implement three stacks.

Yout should implement push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum) methods. stackNum is the index of the stack. value is the value that pushed to the stack.

The constructor requires a stackSize parameter, which represents the size of each stack.

Example1:

 Input:
["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
[[1], [0, 1], [0, 2], [0], [0], [0], [0]]
 Output:
[null, null, null, 1, -1, -1, true]
Explanation: When the stack is empty, `pop, peek` return -1. When the stack is full, `push` does nothing.
Example2:

 Input:
["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
[[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
 Output:
[null, null, null, null, 2, 1, -1, -1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/three-in-one-lcci
"""


class TripleInOne:

    def __init__(self, stackSize: int):
        self.stack = [[], [], []]
        self.stackSize = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if self.stackSize == len(self.stack[stackNum]):
            return
        self.stack[stackNum].append(value)

    def pop(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            return -1
        return self.stack[stackNum].pop()

    def peek(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            return -1
        return self.stack[stackNum][-1]

    def isEmpty(self, stackNum: int) -> bool:
        return len(self.stack[stackNum]) == 0

# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
