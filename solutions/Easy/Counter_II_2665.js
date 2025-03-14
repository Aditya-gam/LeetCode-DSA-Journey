/**
 * Function: createCounter
 * Description: This function accepts an initial integer `init` and returns an object 
 * containing three functions:
 * - `increment()`: Increases the current value by 1 and returns it.
 * - `decrement()`: Decreases the current value by 1 and returns it.
 * - `reset()`: Resets the value to `init` and returns it.
 *
 * @param {number} init - The initial value for the counter.
 * @returns {Object} - An object with `increment`, `decrement`, and `reset` methods.
 */
var createCounter = function(init) {
    let current = init; // Stores the current value

    return {
        increment: function() {
            return ++current;
        },
        decrement: function() {
            return --current;
        },
        reset: function() {
            current = init;
            return current;
        }
    };
};

// Example Test Cases
if (require.main === module) {
    const counter1 = createCounter(5);

    // Test case 1: Basic increment, reset, and decrement operations
    console.log(counter1.increment()); // Expected output: 6
    console.log(counter1.reset());     // Expected output: 5
    console.log(counter1.decrement()); // Expected output: 4

    // Test case 2: Multiple increments and resets
    const counter2 = createCounter(0);
    console.log(counter2.increment()); // Expected output: 1
    console.log(counter2.increment()); // Expected output: 2
    console.log(counter2.decrement()); // Expected output: 1
    console.log(counter2.reset());     // Expected output: 0
    console.log(counter2.reset());     // Expected output: 0

    // Test case 3: Negative starting value
    const counter3 = createCounter(-3);
    console.log(counter3.increment()); // Expected output: -2
    console.log(counter3.increment()); // Expected output: -1
    console.log(counter3.decrement()); // Expected output: -2
    console.log(counter3.reset());     // Expected output: -3

    // Test case 4: Large positive initial value
    const counter4 = createCounter(1000);
    console.log(counter4.decrement()); // Expected output: 999
    console.log(counter4.increment()); // Expected output: 1000
    console.log(counter4.increment()); // Expected output: 1001
    console.log(counter4.reset());     // Expected output: 1000
}

/*

Complexity Analysis:
- Time Complexity: O(1) - Each method performs a single operation (increment, decrement, or reset).
- Space Complexity: O(1) - Only a single variable `current` is stored in memory.

*/