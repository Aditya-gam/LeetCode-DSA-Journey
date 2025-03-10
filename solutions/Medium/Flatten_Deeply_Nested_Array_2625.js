/**
 * Function: flat
 * Description: This function recursively flattens a multi-dimensional array up to a given depth `n`.
 * - If `n` is 0, the array remains unchanged.
 * - Each level of depth removes one layer of nesting until `n` is exhausted.
 *
 * @param {Array} arr - The multi-dimensional input array.
 * @param {number} depth - The maximum depth to flatten.
 * @returns {Array} - The flattened array up to `depth` levels.
 */
const flat = function (arr, depth) {
    if (depth === 0) return arr; // Base case: No flattening if depth is 0

    let result = [];

    for (const item of arr) {
        if (Array.isArray(item) && depth > 0) {
            result.push(...flat(item, depth - 1)); // Recursively flatten subarrays
        } else {
            result.push(item); // Append non-array elements
        }
    }

    return result;
};

// Example Test Cases
if (require.main === module) {
    console.log(flat([1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]], 0));
    // Expected output: [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]

    console.log(flat([1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]], 1));
    // Expected output: [1, 2, 3, 4, 5, 6, 7, 8, [9, 10, 11], 12, 13, 14, 15]

    console.log(flat([[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]], 2));
    // Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    console.log(flat([[[[1, 2], 3], 4], 5], 2));
    // Expected output: [[1, 2], 3, 4, 5]

    console.log(flat([], 3));
    // Expected output: []

    console.log(flat([1, [2, [3, [4]]]], 3));
    // Expected output: [1, 2, 3, [4]]
}

/*

Complexity Analysis:
- Time Complexity: O(n), where `n` is the total number of elements, as each element is visited once.
- Space Complexity: O(n), as a new array is created with flattened elements.

*/

export default flat;
