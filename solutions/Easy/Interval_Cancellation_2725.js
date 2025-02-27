/**
 * Function: cancellable
 * Description: This function repeatedly calls `fn` with `args` immediately and then at 
 * intervals of `t` milliseconds until the cancel function is invoked.
 *
 * @param {Function} fn - The function to be executed at intervals.
 * @param {Array} args - The arguments to be passed to `fn`.
 * @param {number} t - The interval in milliseconds for repeated execution.
 * @returns {Function} - A cancel function that stops the repeated execution of `fn`.
 */
const cancellable = function(fn, args, t) {
    fn(...args); // Call the function immediately
    const intervalId = setInterval(() => fn(...args), t); // Set up repeated execution

    return function cancelFn() {
        clearInterval(intervalId); // Stop execution when cancel function is called
    };
};

// Example Test Cases
if (require.main === module) {
    const result = [];

    const fn1 = (x) => x * 2;
    const args1 = [4], t1 = 35, cancelTimeMs1 = 190;

    const start1 = performance.now();
    const log1 = (...argsArr) => {
        const diff = Math.floor(performance.now() - start1);
        result.push({ "time": diff, "returned": fn1(...argsArr) });
    };

    const cancel1 = cancellable(log1, args1, t1);
    setTimeout(cancel1, cancelTimeMs1);

    setTimeout(() => {
        console.log(result);
        // Expected output: Calls `fn1(4)` every 35ms until 190ms
    }, cancelTimeMs1 + t1 + 15);


    // Test case 2: Function multiplying two numbers
    const result2 = [];
    const fn2 = (x1, x2) => x1 * x2;
    const args2 = [2, 5], t2 = 30, cancelTimeMs2 = 165;

    const start2 = performance.now();
    const log2 = (...argsArr) => {
        const diff = Math.floor(performance.now() - start2);
        result2.push({ "time": diff, "returned": fn2(...argsArr) });
    };

    const cancel2 = cancellable(log2, args2, t2);
    setTimeout(cancel2, cancelTimeMs2);

    setTimeout(() => {
        console.log(result2);
        // Expected output: Calls `fn2(2,5)` every 30ms until 165ms
    }, cancelTimeMs2 + t2 + 15);


    // Test case 3: Function adding three numbers
    const result3 = [];
    const fn3 = (x1, x2, x3) => x1 + x2 + x3;
    const args3 = [5, 1, 3], t3 = 50, cancelTimeMs3 = 180;

    const start3 = performance.now();
    const log3 = (...argsArr) => {
        const diff = Math.floor(performance.now() - start3);
        result3.push({ "time": diff, "returned": fn3(...argsArr) });
    };

    const cancel3 = cancellable(log3, args3, t3);
    setTimeout(cancel3, cancelTimeMs3);

    setTimeout(() => {
        console.log(result3);
        // Expected output: Calls `fn3(5,1,3)` every 50ms until 180ms
    }, cancelTimeMs3 + t3 + 15);
}

/*

Complexity Analysis:
- Time Complexity: O(1) - The function sets an interval and returns immediately.
- Space Complexity: O(1) - Only a reference to the interval ID is stored.

*/

export default cancellable;
