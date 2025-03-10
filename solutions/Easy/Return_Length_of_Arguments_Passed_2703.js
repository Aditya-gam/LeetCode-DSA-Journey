/**
 * Function: argumentsLength
 * Description: This function takes a variable number of arguments and returns the count of arguments passed.
 *
 * @param {...(null|boolean|number|string|Array|Object)} args - Any number of arguments of various types.
 * @returns {number} - The number of arguments passed to the function.
 */
const argumentsLength = function(...args) {
    return args.length;
};

// Example Test Cases
if (require.main === module) {
    // Test case 1: Single argument
    console.log(argumentsLength(5)); 
    // Expected output: 1

    // Test case 2: Multiple arguments of different types
    console.log(argumentsLength({}, null, "3")); 
    // Expected output: 3

    // Test case 3: No arguments
    console.log(argumentsLength()); 
    // Expected output: 0

    // Test case 4: Five arguments
    console.log(argumentsLength(1, 2, 3, 4, 5)); 
    // Expected output: 5

    // Test case 5: Nested array
    console.log(argumentsLength([1, 2, 3], "hello", 42, { a: 1 })); 
    // Expected output: 4
}

/*

Complexity Analysis:
- Time Complexity: O(1) - The function simply returns the length of the `args` array.
- Space Complexity: O(1) - No extra space is used apart from function execution.

*/

export default argumentsLength;
