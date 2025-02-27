/**
 * Function: join
 * Description: This function merges two arrays of objects based on the `id` key.
 * - If an `id` exists in only one array, the object is included as is.
 * - If an `id` exists in both arrays, the properties are merged, with values from `arr2` overriding `arr1`.
 * - The resulting array is sorted in ascending order of `id`.
 *
 * @param {Array} arr1 - First array of objects.
 * @param {Array} arr2 - Second array of objects.
 * @returns {Array} - A merged array sorted by `id`.
 */
const join = function(arr1, arr2) {
    const map = new Map();

    // Insert elements from arr1 into the map
    for (const obj of arr1) {
        map.set(obj.id, obj);
    }

    // Merge elements from arr2 into the map (overwriting if necessary)
    for (const obj of arr2) {
        if (map.has(obj.id)) {
            map.set(obj.id, { ...map.get(obj.id), ...obj });
        } else {
            map.set(obj.id, obj);
        }
    }

    // Convert the map values into a sorted array
    return Array.from(map.values()).sort((a, b) => a.id - b.id);
};

// Example Test Cases
if (require.main === module) {
    console.log(join(
        [{"id": 1, "x": 1}, {"id": 2, "x": 9}], 
        [{"id": 3, "x": 5}]
    ));
    // Expected output: [{"id": 1, "x": 1}, {"id": 2, "x": 9}, {"id": 3, "x": 5}]

    console.log(join(
        [{"id": 1, "x": 2, "y": 3}, {"id": 2, "x": 3, "y": 6}], 
        [{"id": 2, "x": 10, "y": 20}, {"id": 3, "x": 0, "y": 0}]
    ));
    // Expected output: [{"id": 1, "x": 2, "y": 3}, {"id": 2, "x": 10, "y": 20}, {"id": 3, "x": 0, "y": 0}]

    console.log(join(
        [{"id": 1, "b": {"b": 94}, "v": [4, 3], "y": 48}], 
        [{"id": 1, "b": {"c": 84}, "v": [1, 3]}]
    ));
    // Expected output: [{"id": 1, "b": {"c": 84}, "v": [1, 3], "y": 48}]
}

/*

Complexity Analysis:
- Time Complexity: O(n + m + k log k) → O(n + m) for merging and O(k log k) for sorting.
  - `n`: Length of `arr1`
  - `m`: Length of `arr2`
  - `k`: Unique `id` count (n + m in the worst case)
- Space Complexity: O(n + m) → Storing elements in the map.

*/

module.exports = join;
