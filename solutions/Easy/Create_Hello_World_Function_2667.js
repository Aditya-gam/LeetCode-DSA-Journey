/**
 * Function: createHelloWorld
 * Description: This function returns a new function that always returns "Hello World",
 * regardless of any arguments passed to it.
 *
 * @returns {Function} - A function that returns "Hello World".
 */
let createHelloWorld = function() {
    return function(...args) {
        return "Hello World";
    };
};

// Example Test Cases
if (require.main === module) {
    const f = createHelloWorld();

    // Test case 1: Calling without arguments
    console.log(f()); 
    // Expected output: "Hello World"

    // Test case 2: Calling with an empty array as argument
    console.log(f([])); 
    // Expected output: "Hello World"

    // Test case 3: Calling with multiple arguments
    console.log(f({}, null, 42)); 
    // Expected output: "Hello World"

    // Test case 4: Calling with different data types
    console.log(f("test", 100, true, [1, 2, 3])); 
    // Expected output: "Hello World"

    // Test case 5: Calling with no arguments multiple times
    console.log(f()); 
    console.log(f()); 
    // Expected output: "Hello World"
    // Expected output: "Hello World"
}

/*

Complexity Analysis:
- Time Complexity: O(1) - The function always returns a constant value in constant time.
- Space Complexity: O(1) - No extra space is used apart from function allocation.

*/

