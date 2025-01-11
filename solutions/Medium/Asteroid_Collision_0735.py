class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                # Collision happens
                if abs(asteroid) > abs(stack[-1]):
                    stack.pop()  # Top asteroid explodes
                elif abs(asteroid) == abs(stack[-1]):
                    stack.pop()  # Both explode
                    break
                else:
                    # The current asteroid explodes
                    break
            else:
                # No collision, add the asteroid to stack
                stack.append(asteroid)

        return stack


# Example test cases
sol = Solution()
print(sol.asteroidCollision([5, 10, -5]))  # [5, 10]
print(sol.asteroidCollision([8, -8]))  # []
print(sol.asteroidCollision([10, 2, -5]))  # [10]
print(sol.asteroidCollision([-2, -1, 1, 2]))  # [-2, -1, 1, 2]
print(sol.asteroidCollision([-2, 2, -1, -2]))  # [-2]
print(sol.asteroidCollision([1, -1, -2, -2]))  # [-2, -2]

# Complexity Analysis
# Time Complexity: O(n)
# Each asteroid is pushed and popped from the stack at most once, so the time complexity is linear.

# Space Complexity: O(n)
# The stack stores the surviving asteroids, with a maximum size of n.
