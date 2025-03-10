/**
 * Function: reduce
 * Description: This function applies a reducer function `fn` to each element in the array `nums`,
 * accumulating a result starting from `init`. The final accumulated value is returned.
 * It does not use the built-in `Array.reduce()` method.
 *
 * @param {number[]} nums - The input array of numbers.
 * @param {Function} fn - The reducer function that takes two arguments (accumulator, currentValue).
 * @param {number} init - The initial accumulator value.
 * @returns {number} - The final accumulated value after applying `fn` to all elements in `nums`.
 */
let reduce = function(nums, fn, init) {
    let accumulator = init; // Initialize accumulator with init

    for (const num of nums) {
        accumulator = fn(accumulator, num); // Apply function to update accumulator
    }

    return accumulator;
};

// Example Test Cases
if (require.main === module) {
    // Test case 1: Sum of all elements
    const sum = (accum, curr) => accum + curr;
    console.log(reduce([1, 2, 3, 4], sum, 0)); 
    // Expected output: 10

    // Test case 2: Sum with squared numbers
    const sumWithSquares = (accum, curr) => accum + curr * curr;
    console.log(reduce([1, 2, 3, 4], sumWithSquares, 100)); 
    // Expected output: 130

    // Test case 3: Empty array (should return init value)
    console.log(reduce([], sum, 25)); 
    // Expected output: 25

    // Test case 4: Product of all elements
    const product = (accum, curr) => accum * curr;
    console.log(reduce([1, 2, 3, 4], product, 1)); 
    // Expected output: 24

    // Test case 5: Finding the maximum element
    const maxFinder = (accum, curr) => Math.max(accum, curr);
    console.log(reduce([5, 3, 8, 1, 9], maxFinder, -Infinity)); 
    // Expected output: 9

    // Test case 6: Finding the minimum element
    const minFinder = (accum, curr) => Math.min(accum, curr);
    console.log(reduce([5, 3, 8, 1, 9], minFinder, Infinity)); 
    // Expected output: 1
}

/*

Complexity Analysis:
- Time Complexity: O(n) - We iterate through the array once and apply the function to each element.
- Space Complexity: O(1) - The function uses a single accumulator variable and does not allocate extra space.

*/


