/**
 * Function: map
 * Description: This function applies a given transformation function `fn`
 * to each element of the input array `arr` and returns a new transformed array.
 * It does not use the built-in `Array.map` method.
 *
 * @param {number[]} arr - The input array of numbers.
 * @param {Function} fn - The transformation function to apply to each element.
 * @returns {number[]} - A new array with the transformed elements.
 */
let map = function(arr, fn) {
    const result = []; // Initialize an empty array to store the transformed elements

    for (let i = 0; i < arr.length; i++) {
        result.push(fn(arr[i], i)); // Apply the function to each element and push the result
    }

    return result;
};

// Example Test Cases
if (require.main === module) {
    // Test case 1: Increment each element by 1
    const plusOne = (n) => n + 1;
    console.log(map([1, 2, 3], plusOne)); 
    // Expected output: [2, 3, 4]

    // Test case 2: Add the index to each element
    const plusIndex = (n, i) => n + i;
    console.log(map([1, 2, 3], plusIndex)); 
    // Expected output: [1, 3, 5]

    // Test case 3: Return a constant value for all elements
    const constant = () => 42;
    console.log(map([10, 20, 30], constant)); 
    // Expected output: [42, 42, 42]

    // Test case 4: Empty array (edge case)
    console.log(map([], plusOne)); 
    // Expected output: []

    // Test case 5: Negative numbers
    console.log(map([-1, -2, -3], plusOne)); 
    // Expected output: [0, -1, -2]

    // Test case 6: Large numbers
    console.log(map([1000000, 2000000, 3000000], plusIndex)); 
    // Expected output: [1000000, 2000001, 3000002]
}

/*

Complexity Analysis:
- Time Complexity: O(n) - We iterate through the input array once, applying the function to each element.
- Space Complexity: O(n) - A new array is created to store the transformed elements.

*/


