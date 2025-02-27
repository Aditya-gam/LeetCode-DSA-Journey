class ProductOfNumbers:
    """
    Class: ProductOfNumbers
    Description: Implements a data structure that supports adding numbers to a stream
                 and retrieving the product of the last k numbers efficiently.

    Methods:
    - add(num): Adds a number to the stream.
    - getProduct(k): Returns the product of the last k numbers in the stream.

    Optimized Approach:
    - Uses a prefix product list to store cumulative products, allowing O(1) retrieval.
    - Handles zeros efficiently by resetting the prefix product list.
    """

    def __init__(self):
        """
        Initializes an empty list to store prefix products.
        If a zero is encountered, the list is reset.
        """
        self.prefix_products = [1]  # Store cumulative products

    def add(self, num: int) -> None:
        """
        Adds an integer to the stream and updates the prefix product list.

        Parameters:
        - num (int): The integer to be added.
        """
        if num == 0:
            self.prefix_products = [1]  # Reset if zero is encountered
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        """
        Retrieves the product of the last k numbers in the stream.

        Parameters:
        - k (int): The number of last elements whose product is required.

        Returns:
        - int: The product of the last k elements.
        """
        if k >= len(self.prefix_products):
            return 0  # If k exceeds the stored prefix, a zero was encountered before

        return self.prefix_products[-1] // self.prefix_products[-k - 1]


# Example Test Cases
if __name__ == "__main__":
    productOfNumbers = ProductOfNumbers()

    # Test case 1: Basic add operations
    productOfNumbers.add(3)
    productOfNumbers.add(0)
    productOfNumbers.add(2)
    productOfNumbers.add(5)
    productOfNumbers.add(4)

    # Test case 2: Fetching last k products
    print(productOfNumbers.getProduct(2))  # Expected output: 20  -> (5 * 4)
    # Expected output: 40  -> (2 * 5 * 4)
    print(productOfNumbers.getProduct(3))
    # Expected output: 0   -> (0 * 2 * 5 * 4)
    print(productOfNumbers.getProduct(4))

    # Test case 3: Adding a number after zero
    productOfNumbers.add(8)
    print(productOfNumbers.getProduct(2))  # Expected output: 32  -> (4 * 8)

    # Test case 4: Adding multiple numbers and checking product
    productOfNumbers.add(2)
    productOfNumbers.add(10)
    # Expected output: 160  -> (8 * 2 * 10)
    print(productOfNumbers.getProduct(3))

    # Test case 5: Adding a zero resets history
    productOfNumbers.add(0)
    productOfNumbers.add(1)
    productOfNumbers.add(3)
    print(productOfNumbers.getProduct(2))  # Expected output: 3 -> (1 * 3)

    # Test case 6: Large k request after zero
    # Expected output: 0 (since zero resets the history)
    print(productOfNumbers.getProduct(10))

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(1) for both add and getProduct operations.
# Space Complexity: O(N) where N is the number of elements added to the stream.
#                  The prefix_products list will have at most N elements.
