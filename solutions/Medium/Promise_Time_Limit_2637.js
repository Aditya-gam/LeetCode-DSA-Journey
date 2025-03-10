/**
 * Function: timeLimit
 * Description: This function takes an asynchronous function `fn` and a time limit `t` in milliseconds.
 * It returns a new function that ensures `fn` resolves within `t` milliseconds.
 * If `fn` exceeds `t` milliseconds, the function rejects with "Time Limit Exceeded".
 *
 * @param {Function} fn - The asynchronous function to be limited.
 * @param {number} t - The time limit in milliseconds.
 * @returns {Function} - A new function that enforces the time limit on `fn`.
 */
const timeLimit = function(fn, t) {
    return async function(...args) {
        return new Promise((resolve, reject) => {
            const timer = setTimeout(() => reject("Time Limit Exceeded"), t); // Set up timeout rejection

            fn(...args)
                .then((result) => {
                    clearTimeout(timer); // Clear timeout if fn resolves in time
                    resolve(result);
                })
                .catch((err) => {
                    clearTimeout(timer); // Clear timeout if fn throws an error
                    reject(err);
                });
        });
    };
};

// Example Test Cases
if (require.main === module) {
    // Test case 1: Function exceeds time limit and should be rejected
    const fn1 = async (n) => { 
        await new Promise(res => setTimeout(res, 100)); 
        return n * n; 
    };
    const limited1 = timeLimit(fn1, 50);
    const start1 = performance.now();
    limited1(5)
        .then(res => console.log({ "resolved": res, "time": Math.floor(performance.now() - start1) }))
        .catch(err => console.log({ "rejected": err, "time": Math.floor(performance.now() - start1) }));
    // Expected output: {"rejected":"Time Limit Exceeded","time":50}

    // Test case 2: Function resolves before time limit
    const fn2 = async (n) => { 
        await new Promise(res => setTimeout(res, 100)); 
        return n * n; 
    };
    const limited2 = timeLimit(fn2, 150);
    const start2 = performance.now();
    limited2(5)
        .then(res => console.log({ "resolved": res, "time": Math.floor(performance.now() - start2) }))
        .catch(err => console.log({ "rejected": err, "time": Math.floor(performance.now() - start2) }));
    // Expected output: {"resolved":25,"time":100}

    // Test case 3: Function resolving with sum
    const fn3 = async (a, b) => { 
        await new Promise(res => setTimeout(res, 120)); 
        return a + b; 
    };
    const limited3 = timeLimit(fn3, 150);
    const start3 = performance.now();
    limited3(5, 10)
        .then(res => console.log({ "resolved": res, "time": Math.floor(performance.now() - start3) }))
        .catch(err => console.log({ "rejected": err, "time": Math.floor(performance.now() - start3) }));
    // Expected output: {"resolved":15,"time":120}

    // Test case 4: Function throws an error immediately
    const fn4 = async () => { throw new Error("Error"); };
    const limited4 = timeLimit(fn4, 1000);
    const start4 = performance.now();
    limited4()
        .then(res => console.log({ "resolved": res, "time": Math.floor(performance.now() - start4) }))
        .catch(err => console.log({ "rejected": err, "time": Math.floor(performance.now() - start4) }));
    // Expected output: {"rejected":"Error","time":0}
}

/*

Complexity Analysis:
- Time Complexity: O(1) - The function sets a timeout and an async execution.
- Space Complexity: O(1) - Only a timeout ID is stored.

*/

export default timeLimit;
