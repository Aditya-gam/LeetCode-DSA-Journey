class Solution(object):
    def countPrimes(self, n):
        """
        Count the number of prime numbers less than n using the Sieve of Eratosthenes.

        :param n: int - The upper bound (exclusive)
        :return: int - The count of prime numbers less than n
        """
        if n <= 2:
            return 0

        # Initialize a boolean array to mark primes
        is_prime = [True] * n
        is_prime[0], is_prime[1] = False, False  # 0 and 1 are not primes

        # Apply Sieve of Eratosthenes
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # Mark multiples of i as non-prime
                for j in range(i * i, n, i):
                    is_prime[j] = False

        # Count the number of primes
        return sum(is_prime)


# Example test cases
sol = Solution()
print(sol.countPrimes(10))  # Output: 4
print(sol.countPrimes(0))   # Output: 0
print(sol.countPrimes(1))   # Output: 0
print(sol.countPrimes(20))  # Output: 8
print(sol.countPrimes(100))  # Output: 25
print(sol.countPrimes(499979))  # Output: 41537
print(sol.countPrimes(999983))  # Output: 78497
print(sol.countPrimes(1500000))  # Output: 114155

# Complexity Analysis
# Time Complexity: O(nloglogn)
# The Sieve of Eratosthenes algorithm has a time complexity of O(nloglogn).
# The outer loop runs from 2 to sqrt(n), which is O(loglogn).
# The inner loop runs from i^2 to n, which is O(n).

# Space Complexity: O(n)
# The is_prime list requires O(n) space.
# The space complexity can be reduced to O(sqrt(n)) by only marking numbers up to sqrt(n) as non-prime.
