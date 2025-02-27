/**
 * Function: sortBy
 * Description: This function sorts an array `arr` in ascending order based on the values 
 * returned by applying the function `fn` to each element.
 *
 * @param {Array} arr - The input array to be sorted.
 * @param {Function} fn - A function that returns a number to determine the sorting order.
 * @returns {Array} - A sorted array in ascending order based on `fn` output.
 */
const sortBy = function(arr, fn) {
    return arr.slice().sort((a, b) => fn(a) - fn(b));
};

// Example Test Cases
if (require.main === module) {
    console.log(sortBy([5, 4, 1, 2, 3], x => x));
    // Expected output: [1, 2, 3, 4, 5]

    console.log(sortBy([{x: 1}, {x: 0}, {x: -1}], d => d.x));
    // Expected output: [{x: -1}, {x: 0}, {x: 1}]

    console.log(sortBy([[3, 4], [5, 2], [10, 1]], x => x[1]));
    // Expected output: [[10, 1], [5, 2], [3, 4]]

    console.log(sortBy(["apple", "banana", "cherry"], s => s.length));
    // Expected output: ["apple", "cherry", "banana"]

    console.log(sortBy([{age: 30}, {age: 20}, {age: 40}], p => p.age));
    // Expected output: [{age: 20}, {age: 30}, {age: 40}]
}

/*

Complexity Analysis:
- Time Complexity: O(n log n) - Sorting takes O(n log n) in the worst case.
- Space Complexity: O(n) - Since `.slice()` creates a new array before sorting.

*/

module.exports = sortBy;
