/**
 * Function: cancellable
 * Description: This function schedules the execution of `fn` with provided `args` after `t` milliseconds.
 * If the returned cancel function is called before `t` milliseconds, the execution of `fn` is prevented.
 *
 * @param {Function} fn - The function to be executed.
 * @param {Array} args - The arguments to be passed to `fn`.
 * @param {number} t - The delay in milliseconds before executing `fn`.
 * @returns {Function} - A cancel function that prevents `fn` from being executed if called before `t` milliseconds.
 */
const cancellable = function(fn, args, t) {
    const timeoutId = setTimeout(() => fn(...args), t); // Schedule function execution

    return function cancelFn() {
        clearTimeout(timeoutId); // Cancel execution if cancelFn is called
    };
};

// Example Test Cases
if (require.main === module) {
    const result = [];

    const fn1 = (x) => x * 5;
    const args1 = [2], t1 = 20, cancelTimeMs1 = 50;

    const start1 = performance.now();
    const log1 = (...argsArr) => {
        const diff = Math.floor(performance.now() - start1);
        result.push({ "time": diff, "returned": fn1(...argsArr) });
    };

    const cancel1 = cancellable(log1, args1, t1);
    setTimeout(cancel1, cancelTimeMs1);

    const maxT1 = Math.max(t1, cancelTimeMs1);
    setTimeout(() => {
        console.log(result); // Expected output: [{"time":20,"returned":10}]
    }, maxT1 + 15);


    // Test case 2: Cancellation occurs before execution
    const result2 = [];
    const fn2 = (x) => x ** 2;
    const args2 = [2], t2 = 100, cancelTimeMs2 = 50;

    const start2 = performance.now();
    const log2 = (...argsArr) => {
        const diff = Math.floor(performance.now() - start2);
        result2.push({ "time": diff, "returned": fn2(...argsArr) });
    };

    const cancel2 = cancellable(log2, args2, t2);
    setTimeout(cancel2, cancelTimeMs2);

    const maxT2 = Math.max(t2, cancelTimeMs2);
    setTimeout(() => {
        console.log(result2); // Expected output: []
    }, maxT2 + 15);


    // Test case 3: Execution occurs before cancellation
    const result3 = [];
    const fn3 = (x1, x2) => x1 * x2;
    const args3 = [2, 4], t3 = 30, cancelTimeMs3 = 100;

    const start3 = performance.now();
    const log3 = (...argsArr) => {
        const diff = Math.floor(performance.now() - start3);
        result3.push({ "time": diff, "returned": fn3(...argsArr) });
    };

    const cancel3 = cancellable(log3, args3, t3);
    setTimeout(cancel3, cancelTimeMs3);

    const maxT3 = Math.max(t3, cancelTimeMs3);
    setTimeout(() => {
        console.log(result3); // Expected output: [{"time":30,"returned":8}]
    }, maxT3 + 15);
}

/*

Complexity Analysis:
- Time Complexity: O(1) - The function schedules a timeout and returns immediately.
- Space Complexity: O(1) - Only a reference to the timeout ID is stored.

*/

export default cancellable;
