/**
 * Function: once
 * Description: This function takes another function `fn` and returns a modified version 
 * of `fn` that can only be called once. On the first call, it executes `fn` normally.
 * Subsequent calls return `undefined` without calling `fn`.
 *
 * @param {Function} fn - The original function that should only be called once.
 * @returns {Function} - A new function that ensures `fn` is only executed once.
 */
const once = function(fn) {
    let hasBeenCalled = false; // Flag to track if the function has been called
    let result; // Store the first function result

    return function(...args) {
        if (!hasBeenCalled) {
            hasBeenCalled = true;
            result = fn(...args);
            return result;
        }
        return undefined; // Subsequent calls return undefined
    };
};

// Example Test Cases
if (require.main === module) {
    // Test case 1: Sum function (should execute only once)
    let fn1 = (a, b, c) => a + b + c;
    let onceFn1 = once(fn1);
    console.log(onceFn1(1, 2, 3)); // Expected output: 6
    console.log(onceFn1(2, 3, 6)); // Expected output: undefined

    // Test case 2: Multiplication function
    let fn2 = (a, b, c) => a * b * c;
    let onceFn2 = once(fn2);
    console.log(onceFn2(5, 7, 4)); // Expected output: 140
    console.log(onceFn2(2, 3, 6)); // Expected output: undefined
    console.log(onceFn2(4, 6, 8)); // Expected output: undefined

    // Test case 3: Function returning a constant value
    let fn3 = () => 42;
    let onceFn3 = once(fn3);
    console.log(onceFn3()); // Expected output: 42
    console.log(onceFn3()); // Expected output: undefined

    // Test case 4: Function returning a string
    let fn4 = (name) => `Hello, ${name}`;
    let onceFn4 = once(fn4);
    console.log(onceFn4("Alice")); // Expected output: "Hello, Alice"
    console.log(onceFn4("Bob")); // Expected output: undefined
}

/*

Complexity Analysis:
- Time Complexity: O(1) - The function checks a flag and executes only once.
- Space Complexity: O(1) - Only a boolean flag and a result variable are stored.

*/

export default once;
