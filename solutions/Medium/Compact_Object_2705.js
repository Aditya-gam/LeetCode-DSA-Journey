/**
 * Function: compactObject
 * Description: This function removes falsy values (null, 0, false, "", undefined, NaN) from an object or array.
 * - Works recursively to clean nested objects and arrays.
 * - Arrays remain arrays, with falsy elements removed.
 * - Objects remain objects, with falsy key-value pairs removed.
 *
 * @param {Object|Array} obj - The input object or array.
 * @returns {Object|Array} - A new object or array with falsy values removed.
 */
const compactObject = function(obj) {
    if (Array.isArray(obj)) {
        // If obj is an array, filter out falsy values and recursively compact nested elements
        return obj.filter(Boolean).map(compactObject);
    } else if (typeof obj === "object" && obj !== null) {
        // If obj is an object, iterate over keys and remove falsy values
        return Object.fromEntries(
            Object.entries(obj)
                .filter(([_, value]) => Boolean(value)) // Remove falsy values
                .map(([key, value]) => [key, compactObject(value)]) // Recursively clean nested structures
        );
    }
    return obj; // Return non-object, non-array values as is
};

// Example Test Cases
if (require.main === module) {
    console.log(compactObject([null, 0, false, 1]));
    // Expected output: [1]

    console.log(compactObject({"a": null, "b": [false, 1]}));
    // Expected output: {"b": [1]}

    console.log(compactObject([null, 0, 5, [0], [false, 16]]));
    // Expected output: [5, [], [16]]

    console.log(compactObject({"x": 0, "y": {"a": false, "b": 2}, "z": [NaN, "", "hello"]}));
    // Expected output: {"y": {"b": 2}, "z": ["hello"]}

    console.log(compactObject({"a": undefined, "b": {"c": "", "d": 4}, "e": []}));
    // Expected output: {"b": {"d": 4}}

    console.log(compactObject([]));
    // Expected output: []

    console.log(compactObject({}));
    // Expected output: {}
}

/*

Complexity Analysis:
- Time Complexity: O(n), where `n` is the number of elements/keys in `obj`, as we traverse each element once.
- Space Complexity: O(n), since we create a new object/array with non-falsy elements.

*/

export default compactObject;
