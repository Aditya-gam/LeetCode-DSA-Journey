/**
 * Function: filter
 * Description: This function filters elements from the given array `arr` based on the provided filtering function `fn`.
 * It does not use the built-in `Array.filter()` method.
 *
 * @param {number[]} arr - The input array of numbers.
 * @param {Function} fn - The filtering function that determines whether an element should be included.
 * @returns {number[]} - A new array containing elements that satisfy `fn`.
 */
let filter = function(arr, fn) {
    const filteredArr = []; // Initialize an empty array to store filtered elements

    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) { // Apply the function to check truthiness
            filteredArr.push(arr[i]); // Add element to result if the condition is met
        }
    }

    return filteredArr;
};

// Example Test Cases
if (require.main === module) {
    // Test case 1: Filter numbers greater than 10
    const greaterThan10 = (n) => n > 10;
    console.log(filter([0, 10, 20, 30], greaterThan10)); 
    // Expected output: [20, 30]

    // Test case 2: Only keep elements at index 0
    const firstIndex = (n, i) => i === 0;
    console.log(filter([1, 2, 3], firstIndex)); 
    // Expected output: [1]

    // Test case 3: Remove falsy values (0 should be removed)
    const plusOne = (n) => n + 1;
    console.log(filter([-2, -1, 0, 1, 2], plusOne)); 
    // Expected output: [-2, 0, 1, 2]

    // Test case 4: Empty array (edge case)
    console.log(filter([], greaterThan10)); 
    // Expected output: []

    // Test case 5: Keep even numbers
    const isEven = (n) => n % 2 === 0;
    console.log(filter([1, 2, 3, 4, 5, 6], isEven)); 
    // Expected output: [2, 4, 6]

    // Test case 6: Large negative numbers
    const isNegative = (n) => n < 0;
    console.log(filter([-100, -50, 0, 50, 100], isNegative)); 
    // Expected output: [-100, -50]
}

/*

Complexity Analysis:
- Time Complexity: O(n) - We iterate through the input array once and apply the function to each element.
- Space Complexity: O(n) - A new array is created to store the filtered elements.

*/


