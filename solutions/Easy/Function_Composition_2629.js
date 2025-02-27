/**
 * Function: compose
 * Description: This function takes an array of functions and returns a new function
 * that represents their composition. The functions are applied from right to left.
 * If the array is empty, the returned function is an identity function (returns `x`).
 *
 * @param {Function[]} functions - An array of functions to be composed.
 * @returns {Function} - A function that applies the composition of all given functions.
 */
const compose = function(functions) {
    return function(x) {
        return functions.reduceRight((acc, fn) => fn(acc), x);
    };
};

// Example Test Cases
if (require.main === module) {
    // Test case 1: Applying functions from right to left
    const fn1 = compose([x => x + 1, x => x * x, x => 2 * x]);
    console.log(fn1(4)); 
    // Expected output: 65
    // Steps:
    // 2 * 4 = 8
    // 8 * 8 = 64
    // 64 + 1 = 65

    // Test case 2: All functions multiplying by 10
    const fn2 = compose([x => 10 * x, x => 10 * x, x => 10 * x]);
    console.log(fn2(1)); 
    // Expected output: 1000
    // Steps:
    // 10 * 1 = 10
    // 10 * 10 = 100
    // 10 * 100 = 1000

    // Test case 3: Empty function array (identity function)
    const fn3 = compose([]);
    console.log(fn3(42)); 
    // Expected output: 42

    // Test case 4: Single function in the array
    const fn4 = compose([x => x + 5]);
    console.log(fn4(10)); 
    // Expected output: 15

    // Test case 5: Function array with a mix of operations
    const fn5 = compose([x => x - 3, x => x * 2, x => x + 10]);
    console.log(fn5(5)); 
    // Expected output: 17
    // Steps:
    // 5 + 10 = 15
    // 15 * 2 = 30
    // 30 - 3 = 27
}

/*

Complexity Analysis:
- Time Complexity: O(n) - We iterate through the `functions` array once (in reverse order).
- Space Complexity: O(1) - Only a single accumulator variable is maintained.

*/

export default compose;
