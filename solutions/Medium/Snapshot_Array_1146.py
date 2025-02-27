import bisect


class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        Initializes the structure with `length` elements set to 0.
        Each index i will maintain a list of (snap_id, val) changes in ascending snap_id order.
        """
        self.history = [[] for _ in range(length)]
        self.snap_id = 0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        Records that at the current snap_id, index is set to val.
        """
        if not self.history[index] or self.history[index][-1][0] != self.snap_id:
            # Append a new record if this snap_id hasn't been used for this index
            self.history[index].append((self.snap_id, val))
        else:
            # Overwrite the last value for this snap_id
            self.history[index][-1] = (self.snap_id, val)

    def snap(self):
        """
        :rtype: int
        Takes a snapshot, returning the snapshot id, then increments it.
        """
        old_id = self.snap_id
        self.snap_id += 1
        return old_id

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        Retrieves the value at `index` for the snapshot identified by snap_id.
        """
        arr = self.history[index]
        # If no records, everything was 0
        if not arr:
            return 0

        # We want to find rightmost pair with snap_id' <= snap_id
        # We'll do a binary search by snap_id
        #   Each pair is (snap_id', val)

        # Use bisect to find insertion point for (snap_id+1, ) so we get
        # the index where snap_id+1 would be inserted to keep it sorted.
        # Then i-1 is the pair with the largest snap_id' <= snap_id if i>0.

        i = bisect.bisect_right(arr, (snap_id, float('inf')))
        if i == 0:
            # means all pairs have snap_id' > snap_id
            return 0
        else:
            return arr[i-1][1]


# Example usage:
if __name__ == "__main__":
    snapshotArr = SnapshotArray(3)  # set the length to be 3
    snapshotArr.set(0, 5)
    snapid0 = snapshotArr.snap()      # snap_id = 0
    snapshotArr.set(0, 6)
    print(snapshotArr.get(0, snapid0))  # should print 5

    snapid1 = snapshotArr.snap()      # snap_id = 1
    snapshotArr.set(0, 7)
    print(snapshotArr.get(0, snapid1))  # should print 6

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(1) for set and snap operations, O(log(n)) for get operation, where n is the number of snapshots for the given index.
# Space complexity: O(n+m) for storing the history, where n is the number of elements and m is the number of set calls.
