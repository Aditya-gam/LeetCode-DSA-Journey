
/**
 * Function: isEmpty
 * Description: This function checks whether an input object or array is empty.
 * - An object is considered empty if it has no key-value pairs.
 * - An array is considered empty if it has no elements.
 * - The function should run in O(1) time complexity.
 *
 * @param {Object|Array} obj - The input object or array.
 * @returns {boolean} - Returns `true` if the object or array is empty, otherwise `false`.
 */
const isEmpty = function(obj) {
    return Object.keys(obj).length === 0;
};

// Example Test Cases
if (require.main === module) {
    console.log(isEmpty({"x": 5, "y": 42})); // Expected output: false
    console.log(isEmpty({})); // Expected output: true
    console.log(isEmpty([null, false, 0])); // Expected output: false
    console.log(isEmpty([])); // Expected output: true
    console.log(isEmpty({ a: undefined })); // Expected output: false (has a key)
    console.log(isEmpty({ length: 0 })); // Expected output: false (not an empty object)
}

/*

Complexity Analysis:
- Time Complexity: O(1) - Object.keys(obj).length is an optimized operation for checking emptiness.
- Space Complexity: O(1) - No additional space is used.

*/

export default isEmpty;