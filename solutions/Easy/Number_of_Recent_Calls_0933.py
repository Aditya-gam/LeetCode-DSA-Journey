from collections import deque


class RecentCounter(object):

    def __init__(self):
        """
        Initialize the RecentCounter with an empty queue.
        """
        self.requests = deque()

    def ping(self, t):
        """
        Add a new request at time t and return the number of recent requests within the last 3000 milliseconds.

        :type t: int
        :rtype: int
        """
        # Add the current request to the queue
        self.requests.append(t)

        # Remove requests that are outside the range [t-3000, t]
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        # Return the number of valid requests in the range
        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# Example test cases
obj = RecentCounter()
print(obj.ping(1))  # 1
print(obj.ping(100))  # 2
print(obj.ping(3001))  # 3
print(obj.ping(3002))  # 3
print(obj.ping(3003))  # 4
print(obj.ping(3004))  # 5
