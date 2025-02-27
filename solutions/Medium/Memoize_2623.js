/**
 * Function: memoize
 * Description: This function takes another function `fn` and returns a memoized version of `fn`.
 * The memoized function stores results for previously seen inputs, ensuring that 
 * `fn` is never called more than once for the same arguments.
 *
 * @param {Function} fn - The original function to be memoized.
 * @returns {Function} - A memoized version of `fn` that caches results.
 */
function memoize(fn) {
    const cache = new Map(); // Cache to store computed results
    let callCount = 0; // Counter to track function calls

    const memoizedFunction = function(...args) {
        const key = JSON.stringify(args); // Convert arguments to a string key for caching

        if (cache.has(key)) {
            return cache.get(key); // Return cached result if found
        }

        callCount++; // Increment function call count
        const result = fn(...args); // Compute the function result
        cache.set(key, result); // Store result in cache
        return result;
    };

    // Method to retrieve call count
    memoizedFunction.getCallCount = function() {
        return callCount;
    };

    return memoizedFunction;
}

// Example Test Cases
if (require.main === module) {
    // Test case 1: Memoizing sum function
    let callCount1 = 0;
    const sum = (a, b) => { callCount1++; return a + b; };
    const memoizedSum = memoize(sum);
    console.log(memoizedSum(2, 2)); // Expected output: 4
    console.log(memoizedSum(2, 2)); // Expected output: 4 (from cache)
    console.log(memoizedSum.getCallCount()); // Expected output: 1
    console.log(memoizedSum(1, 2)); // Expected output: 3
    console.log(memoizedSum.getCallCount()); // Expected output: 2

    // Test case 2: Memoizing factorial function
    let callCount2 = 0;
    const factorial = (n) => {
        callCount2++;
        return n <= 1 ? 1 : n * factorial(n - 1);
    };
    const memoizedFactorial = memoize(factorial);
    console.log(memoizedFactorial(2)); // Expected output: 2
    console.log(memoizedFactorial(3)); // Expected output: 6
    console.log(memoizedFactorial(2)); // Expected output: 2 (from cache)
    console.log(memoizedFactorial.getCallCount()); // Expected output: 2
    console.log(memoizedFactorial(3)); // Expected output: 6 (from cache)
    console.log(memoizedFactorial.getCallCount()); // Expected output: 2

    // Test case 3: Memoizing Fibonacci function
    let callCount3 = 0;
    const fib = (n) => {
        callCount3++;
        return n <= 1 ? 1 : fib(n - 1) + fib(n - 2);
    };
    const memoizedFib = memoize(fib);
    console.log(memoizedFib(5)); // Expected output: 8
    console.log(memoizedFib.getCallCount()); // Expected output: 1 (memoized)
}

/*

Complexity Analysis:
- Time Complexity: O(1) for repeated calls due to caching. The first call is dependent on `fn`.
- Space Complexity: O(n) in the worst case, storing unique function calls in the cache.

*/

export default memoize;
