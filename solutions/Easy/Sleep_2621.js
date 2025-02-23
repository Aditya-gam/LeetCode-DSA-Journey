/**
 * Function: sleep
 * Description: This function takes a positive integer `millis` and returns a Promise
 * that resolves after `millis` milliseconds.
 *
 * @param {number} millis - The number of milliseconds to sleep.
 * @returns {Promise} - A promise that resolves after `millis` milliseconds.
 */
async function sleep(millis) {
    return new Promise(resolve => setTimeout(resolve, millis));
}

// Example Test Cases
if (require.main === module) {
    let t1 = Date.now();
    sleep(100).then(() => console.log(Date.now() - t1)); 
    // Expected output: ~100

    let t2 = Date.now();
    sleep(200).then(() => console.log(Date.now() - t2)); 
    // Expected output: ~200

    let t3 = Date.now();
    sleep(500).then(() => console.log(Date.now() - t3)); 
    // Expected output: ~500

    let t4 = Date.now();
    sleep(1000).then(() => console.log(Date.now() - t4)); 
    // Expected output: ~1000
}

/*

Complexity Analysis:
- Time Complexity: O(1) - The function does not perform iterative operations.
- Space Complexity: O(1) - No additional space is allocated apart from the timer.

*/

export default sleep;
