class MinStack:
    """
    Class: MinStack
    Description: Implements a stack that supports push, pop, top, and retrieving 
                 the minimum element in constant O(1) time complexity.

    Methods:
    - push(val): Pushes an element onto the stack.
    - pop(): Removes the top element from the stack.
    - top(): Returns the top element of the stack.
    - getMin(): Retrieves the minimum element in the stack.
    """

    def __init__(self):
        """
        Initializes an empty stack and a helper stack to track minimum values.
        """
        self.stack = []
        self.min_stack = []  # Maintains the minimum value at each level

    def push(self, val: int) -> None:
        """
        Pushes an element onto the stack and updates the min_stack.

        Parameters:
        - val (int): The integer value to be pushed onto the stack.
        """
        self.stack.append(val)
        # Push the minimum value onto min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Removes the top element from the stack and updates min_stack.
        """
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        """
        Returns the top element of the stack.

        Returns:
        - int: The top element of the stack.
        """
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        """
        Retrieves the minimum element from the stack.

        Returns:
        - int: The minimum value in the stack.
        """
        return self.min_stack[-1] if self.min_stack else None


# Example Test Cases
if __name__ == "__main__":
    minStack = MinStack()

    # Test case 1: Basic push and getMin operations
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # Expected output: -3

    # Test case 2: Popping and retrieving top and minimum
    minStack.pop()
    print(minStack.top())  # Expected output: 0
    print(minStack.getMin())  # Expected output: -2

    # Test case 3: Single element stack
    singleStack = MinStack()
    singleStack.push(5)
    print(singleStack.getMin())  # Expected output: 5
    print(singleStack.top())  # Expected output: 5
    singleStack.pop()
    print(singleStack.getMin())  # Expected output: None

    # Test case 4: Multiple elements with duplicate min values
    multiStack = MinStack()
    multiStack.push(3)
    multiStack.push(1)
    multiStack.push(1)
    multiStack.push(2)
    print(multiStack.getMin())  # Expected output: 1
    multiStack.pop()
    print(multiStack.getMin())  # Expected output: 1
    multiStack.pop()
    print(multiStack.getMin())  # Expected output: 3

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(1) for all operations (push, pop, top, and getMin).
# Space Complexity: O(N) where N is the number of elements in the stack. The min_stack will also have at most N elements.
