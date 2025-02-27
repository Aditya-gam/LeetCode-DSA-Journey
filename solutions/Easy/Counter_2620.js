/**
 * Function: createCounter
 * Description: This function takes an integer `n` and returns a counter function.
 * The counter function initially returns `n` and increments by 1 on each subsequent call.
 *
 * @param {number} n - The starting value of the counter.
 * @returns {Function} - A function that returns the next value in the sequence each time it is called.
 */
let createCounter = function(n) {
    return function() {
        return n++;
    };
};

// Example Test Cases
if (require.main === module) {
    const counter1 = createCounter(10);

    // Test case 1: Starting from 10
    console.log(counter1()); // Expected output: 10
    console.log(counter1()); // Expected output: 11
    console.log(counter1()); // Expected output: 12
    console.log(counter1()); // Expected output: 13

    // Test case 2: Starting from -2
    const counter2 = createCounter(-2);
    console.log(counter2()); // Expected output: -2
    console.log(counter2()); // Expected output: -1
    console.log(counter2()); // Expected output: 0
    console.log(counter2()); // Expected output: 1
    console.log(counter2()); // Expected output: 2

    // Test case 3: Starting from 0
    const counter3 = createCounter(0);
    console.log(counter3()); // Expected output: 0
    console.log(counter3()); // Expected output: 1
    console.log(counter3()); // Expected output: 2

    // Test case 4: Large positive number
    const counter4 = createCounter(999);
    console.log(counter4()); // Expected output: 999
    console.log(counter4()); // Expected output: 1000
    console.log(counter4()); // Expected output: 1001
}

/*

Complexity Analysis:
- Time Complexity: O(1) - Each function call returns and increments a variable in constant time.
- Space Complexity: O(1) - No additional space is used apart from the function itself.

*/


