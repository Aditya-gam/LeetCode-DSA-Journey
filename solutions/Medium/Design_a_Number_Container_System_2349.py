import heapq


class NumberContainers(object):

    def __init__(self):
        """
        indexToNumber: maps index -> number
        numberToHeap: maps number -> min-heap of indices
        """
        self.indexToNumber = {}
        self.numberToHeap = {}

    def change(self, index, number):
        """
        Assign 'number' to the container at 'index'.
        If 'index' was already assigned a different number, replace it.
        """
        # If index already exists, check if we're replacing a different number
        if index in self.indexToNumber:
            oldNumber = self.indexToNumber[index]
            if oldNumber == number:
                return  # No change needed

        # Update indexToNumber
        self.indexToNumber[index] = number

        # Add index to the min-heap of the new number
        if number not in self.numberToHeap:
            self.numberToHeap[number] = []
        heapq.heappush(self.numberToHeap[number], index)

    def find(self, number):
        """
        Return the smallest index that is currently assigned 'number',
        or -1 if none exists.
        """
        if number not in self.numberToHeap:
            return -1

        minHeap = self.numberToHeap[number]

        # Lazy deletion: pop from heap while top is invalid
        while minHeap:
            topIdx = minHeap[0]
            # Check if top index is still assigned to 'number'
            if self.indexToNumber.get(topIdx, None) == number:
                return topIdx
            else:
                # Pop invalid top index
                heapq.heappop(minHeap)

        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index, number)
# param_2 = obj.find(number)


# Example test cases
if __name__ == "__main__":
    nc = NumberContainers()
    # The example from the prompt
    print(nc.find(10))  # -1 (no index with 10 yet)
    nc.change(2, 10)
    nc.change(1, 10)
    nc.change(3, 10)
    nc.change(5, 10)
    print(nc.find(10))  # 1 (smallest index assigned to 10)
    nc.change(1, 20)
    print(nc.find(10))  # 2 (since index 1 is no longer 10, next smallest is 2)

    # Additional test cases
    nc.change(7, 20)
    nc.change(4, 20)
    print(nc.find(20))  # 4 (smallest index assigned to 20)
    nc.change(4, 30)
    print(nc.find(20))  # 7 (since index 4 is no longer 20, next smallest is 7)
    print(nc.find(30))  # 4 (smallest index assigned to 30)
    print(nc.find(40))  # -1 (no index with 40 yet)


# Complexity analysis
# Time complexity: O(log n) for change() and O(1) for find(), where n is the number of indices assigned to the number.
# Space complexity: O(n) for storing the indices assigned to the number.
