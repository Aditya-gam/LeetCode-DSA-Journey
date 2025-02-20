/**
 * Function: Array.prototype.last
 * Description: Enhances the Array prototype to include a `last()` method.
 * - Returns the last element of the array.
 * - If the array is empty, returns `-1`.
 *
 * @returns {null|boolean|number|string|Array|Object} - The last element of the array or `-1` if empty.
 */
Array.prototype.last = function() {
    return this.length === 0 ? -1 : this[this.length - 1];
};

// Example Test Cases
if (require.main === module) {
    console.log([null, {}, 3].last()); // Expected output: 3
    console.log([].last()); // Expected output: -1
    console.log([1, 2, 3, 4, 5].last()); // Expected output: 5
    console.log(["hello", "world"].last()); // Expected output: "world"
    console.log([[1, 2], [3, 4]].last()); // Expected output: [3, 4]
    console.log([true, false, true].last()); // Expected output: true
}

/*

Complexity Analysis:
- Time Complexity: O(1) - Accessing the last element is constant time.
- Space Complexity: O(1) - No additional memory is allocated.

*/
