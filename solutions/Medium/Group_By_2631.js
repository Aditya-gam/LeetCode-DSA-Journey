/**
 * Function: Array.prototype.groupBy
 * Description: Enhances the `Array` prototype to include a `groupBy(fn)` method.
 * - Groups array elements based on the return value of `fn`.
 * - Each key is the output of `fn(element)`, and the value is an array of elements with that key.
 *
 * @param {Function} fn - A function that takes an array element and returns a string key.
 * @returns {Object} - An object where keys are the results of `fn` and values are arrays of matching elements.
 */
function groupBy(array, fn) {
    const grouped = {};
    
    for (const element of array) {
        const key = fn(element); // Get key from function
        if (!grouped[key]) {
            grouped[key] = [];
        }
        grouped[key].push(element); // Group elements under the key
    }

    return grouped;
}

// Example Test Cases
if (require.main === module) {
    console.log(groupBy([{"id":"1"}, {"id":"1"}, {"id":"2"}], item => item.id));
    // Expected output: { "1": [{"id": "1"}, {"id": "1"}], "2": [{"id": "2"}] }

    console.log([
        [1, 2, 3],
        [1, 3, 5],
        [1, 5, 9]
    ], list => String(list[0]));
    // Expected output: { "1": [[1, 2, 3], [1, 3, 5], [1, 5, 9]] }

    console.log(groupBy([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n => String(n > 5)));
    // Expected output: { "true": [6, 7, 8, 9, 10], "false": [1, 2, 3, 4, 5] }

    console.log(groupBy([1, 2, 3], String));
    // Expected output: { "1": [1], "2": [2], "3": [3] }

    console.log(groupBy([], String));
    // Expected output: {}
}

/*

Complexity Analysis:
- Time Complexity: O(n) - Iterates through the array once.
- Space Complexity: O(n) - Stores grouped elements in an object.

*/


