"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

class MinStack:

    def __init__(self):
        

    def push(self, val: int) -> None:
        

    def pop(self) -> None:
        

    def top(self) -> int:
        

    def getMin(self) -> int:
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
        
"""
class MinStack:
    def __init__(self):  
        self.stack = [] # create a stack
        self.minValue = [] #create a minValue stack that tracks lowest seen value
        pass

    def push(self, val: int) -> None:
        self.stack.append(val) # append the pushed vale
        if self.minValue: # append the value if lower than previous
            self.minValue.append(min(self.minValue[-1],val))
        else:
            self.minValue.append(val)


    def pop(self) -> None:
        self.stack.pop() # pop values
        self.minValue.pop()

    def top(self) -> int:
        return self.stack[-1] #return top of stack

    def getMin(self) -> int:
        return self.minValue[-1] #return top of minValue Stack
