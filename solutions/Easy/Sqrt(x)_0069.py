class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        low, high = 1, x // 2
        result = 1

        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                result = mid  # store the last valid mid
                low = mid + 1
            else:
                high = mid - 1

        return result
