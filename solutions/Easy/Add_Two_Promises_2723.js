/**
 * Function: addTwoPromises
 * Description: This function takes two promises that resolve to numbers and returns a new promise
 * that resolves to the sum of the two resolved values.
 *
 * @param {Promise} promise1 - A promise that resolves to a number.
 * @param {Promise} promise2 - A promise that resolves to a number.
 * @returns {Promise} - A promise that resolves to the sum of the resolved values of `promise1` and `promise2`.
 */
const addTwoPromises = async function(promise1, promise2) {
    const [value1, value2] = await Promise.all([promise1, promise2]); // Resolve both promises concurrently
    return value1 + value2; // Return their sum
};

// Example Test Cases
if (require.main === module) {
    // Test case 1: Simple sum of two resolved promises
    addTwoPromises(Promise.resolve(2), Promise.resolve(2))
        .then(console.log); 
    // Expected output: 4

    // Test case 2: Two different numbers
    addTwoPromises(Promise.resolve(10), Promise.resolve(-12))
        .then(console.log); 
    // Expected output: -2

    // Test case 3: Delayed resolution
    addTwoPromises(
        new Promise(resolve => setTimeout(() => resolve(2), 20)), 
        new Promise(resolve => setTimeout(() => resolve(5), 60))
    ).then(console.log);
    // Expected output: 7

    // Test case 4: Large numbers
    addTwoPromises(Promise.resolve(1000), Promise.resolve(5000))
        .then(console.log); 
    // Expected output: 6000

    // Test case 5: Negative numbers
    addTwoPromises(Promise.resolve(-3), Promise.resolve(-7))
        .then(console.log); 
    // Expected output: -10
}

/*

Complexity Analysis:
- Time Complexity: O(1) - The function awaits both promises concurrently in constant time.
- Space Complexity: O(1) - Only a fixed number of variables are used.

*/

export default addTwoPromises;
