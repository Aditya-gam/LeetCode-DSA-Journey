/**
 * Function: Array.prototype.last
 * Description: Enhances the Array prototype to include a `last()` method.
 * - Returns the last element of the array.
 * - If the array is empty, returns `-1`.
 *
 * @returns {null|boolean|number|string|Array|Object} - The last element of the array or `-1` if empty.
 */
function arrayLast(arr) {
    return arr.length === 0 ? -1 : arr[arr.length - 1];
}

// Example Test Cases
if (require.main === module) {
    console.log(arrayLast([null, {}, 3])); // Expected output: 3
    console.log(arrayLast([])); // Expected output: -1
    console.log(arrayLast([1, 2, 3, 4, 5])); // Expected output: 5
    console.log(arrayLast(["hello", "world"])); // Expected output: "world"
    console.log(arrayLast([[1, 2], [3, 4]])); // Expected output: [3, 4]
    console.log(arrayLast([true, false, true])); // Expected output: true
}

/*

Complexity Analysis:
- Time Complexity: O(1) - Accessing the last element is constant time.
- Space Complexity: O(1) - No additional memory is allocated.

*/
