/**
 * Function: promiseAll
 * Description: This function takes an array of functions that return promises and executes all of them in parallel.
 * It resolves with an array of resolved values in order or rejects with the first error encountered.
 * This is implemented without using `Promise.all`.
 *
 * @param {Array<Function>} functions - An array of functions that return promises.
 * @returns {Promise<any[]>} - A promise that resolves with an array of resolved values or rejects with the first error.
 */
const promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const results = new Array(functions.length);
        let completedCount = 0;
        let hasRejected = false;

        functions.forEach((fn, index) => {
            fn()
                .then((value) => {
                    if (hasRejected) return; // Stop processing if already rejected
                    results[index] = value;
                    completedCount++;

                    if (completedCount === functions.length) {
                        resolve(results); // Resolve only when all promises are fulfilled
                    }
                })
                .catch((error) => {
                    if (!hasRejected) {
                        hasRejected = true;
                        reject(error); // Reject immediately on the first failure
                    }
                });
        });
    });
};

// Example Test Cases
if (require.main === module) {
    const start = performance.now();

    // Test case 1: All functions resolve successfully
    promiseAll([
        () => new Promise(resolve => setTimeout(() => resolve(4), 50)), 
        () => new Promise(resolve => setTimeout(() => resolve(10), 150)), 
        () => new Promise(resolve => setTimeout(() => resolve(16), 100))
    ]).then(res => console.log({ "t": Math.floor(performance.now() - start), "resolved": res }))
    .catch(err => console.log({ "t": Math.floor(performance.now() - start), "rejected": err }));
    // Expected output: { t: 150, resolved: [4, 10, 16] }

    // Test case 2: One function rejects
    const start2 = performance.now();
    promiseAll([
        () => new Promise(resolve => setTimeout(() => resolve(1), 200)), 
        () => new Promise((_, reject) => setTimeout(() => reject("Error"), 100))
    ]).then(res => console.log({ "t": Math.floor(performance.now() - start2), "resolved": res }))
    .catch(err => console.log({ "t": Math.floor(performance.now() - start2), "rejected": err }));
    // Expected output: { t: 100, rejected: "Error" }

    // Test case 3: Single function resolves
    const start3 = performance.now();
    promiseAll([
        () => new Promise(resolve => setTimeout(() => resolve(5), 200))
    ]).then(res => console.log({ "t": Math.floor(performance.now() - start3), "resolved": res }))
    .catch(err => console.log({ "t": Math.floor(performance.now() - start3), "rejected": err }));
    // Expected output: { t: 200, resolved: [5] }
}

/*

Complexity Analysis:
- Time Complexity: O(n) - Each function is called once and we wait for their completion.
- Space Complexity: O(n) - We store the results of each function in an array.

*/

export default promiseAll;
