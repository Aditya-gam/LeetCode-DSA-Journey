/**
 * Function: chunk
 * Description: This function takes an array `arr` and splits it into subarrays of length `size`.
 * - If `arr.length` is not a multiple of `size`, the last subarray may be shorter.
 * - If `arr` is empty, an empty array is returned.
 *
 * @param {Array} arr - The input array to be chunked.
 * @param {number} size - The size of each chunk.
 * @returns {Array} - A chunked array.
 */
const chunk = function(arr, size) {
    const result = [];
    
    for (let i = 0; i < arr.length; i += size) {
        result.push(arr.slice(i, i + size)); // Extract chunks using slice
    }

    return result;
};

// Example Test Cases
if (require.main === module) {
    console.log(chunk([1, 2, 3, 4, 5], 1)); 
    // Expected output: [[1], [2], [3], [4], [5]]

    console.log(chunk([1, 9, 6, 3, 2], 3)); 
    // Expected output: [[1, 9, 6], [3, 2]]

    console.log(chunk([8, 5, 3, 2, 6], 6)); 
    // Expected output: [[8, 5, 3, 2, 6]]

    console.log(chunk([], 1)); 
    // Expected output: []

    console.log(chunk([10, 20, 30, 40, 50, 60, 70], 2)); 
    // Expected output: [[10, 20], [30, 40], [50, 60], [70]]

    console.log(chunk([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)); 
    // Expected output: [[1, 2, 3, 4], [5, 6, 7, 8], [9]]
}

/*

Complexity Analysis:
- Time Complexity: O(n) - Iterates through the array once.
- Space Complexity: O(n) - Stores `n` elements across multiple subarrays.

*/

export default chunk;
