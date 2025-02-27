/**
 * Function: debounce
 * Description: This function takes a function `fn` and a time delay `t` in milliseconds.
 * It returns a debounced version of `fn` that will execute only after `t` milliseconds
 * have passed since the last call. If the function is called again within `t` milliseconds,
 * the previous execution is canceled, and the timer resets.
 *
 * @param {Function} fn - The function to be debounced.
 * @param {number} t - The debounce delay in milliseconds.
 * @returns {Function} - A debounced version of `fn`.
 */
const debounce = function(fn, t) {
    let timerId; // Stores the timeout ID

    return function(...args) {
        clearTimeout(timerId); // Cancel the previous timeout
        timerId = setTimeout(() => fn(...args), t); // Reset timeout with new call
    };
};

// Example Test Cases
if (require.main === module) {
    let start = Date.now();
    function log(...inputs) { 
        console.log([Date.now() - start, inputs]);
    }

    console.log("Test Case 1: ");
    const dlog1 = debounce(log, 50);
    setTimeout(() => dlog1(1), 50);
    setTimeout(() => dlog1(2), 75);
    // Expected Output: [125, [2]] (first call is canceled, second call executes at 125ms)

    console.log("Test Case 2: ");
    const dlog2 = debounce(log, 20);
    setTimeout(() => dlog2(1), 50);
    setTimeout(() => dlog2(2), 100);
    // Expected Output: [70, [1]], [120, [2]]

    console.log("Test Case 3: ");
    const dlog3 = debounce(log, 150);
    setTimeout(() => dlog3(1, 2), 50);
    setTimeout(() => dlog3(3, 4), 300);
    setTimeout(() => dlog3(5, 6), 300);
    // Expected Output: [200, [1,2]], [450, [5,6]]
}

/*

Complexity Analysis:
- Time Complexity: O(1) - Only a single timer is maintained, and operations are constant-time.
- Space Complexity: O(1) - Only one timer reference is stored.

*/

export default debounce;
