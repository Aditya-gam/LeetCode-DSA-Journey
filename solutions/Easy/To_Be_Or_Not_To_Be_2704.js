/**
 * Function: expect
 * Description: This function takes a value and returns an object with two methods:
 * - toBe(val): Checks if the stored value strictly equals `val`. Throws an error if not.
 * - notToBe(val): Checks if the stored value does not strictly equal `val`. Throws an error if it does.
 *
 * @param {*} val - The value to be tested.
 * @returns {Object} - An object with methods toBe and notToBe for assertion testing.
 */
let expect = function(val) {
    return {
        toBe: function(expected) {
            if (val !== expected) {
                throw new Error("Not Equal");
            }
            return true;
        },
        notToBe: function(expected) {
            if (val === expected) {
                throw new Error("Equal");
            }
            return true;
        }
    };
};

// Example Test Cases
if (require.main === module) {
    try {
        console.log(expect(5).toBe(5)); // Expected output: true
    } catch (error) {
        console.error(error.message);
    }

    try {
        console.log(expect(5).notToBe(5)); // Expected to throw "Equal"
    } catch (error) {
        console.error(error.message); // Expected output: "Equal"
    }

    try {
        console.log(expect(5).toBe(null)); // Expected to throw "Not Equal"
    } catch (error) {
        console.error(error.message); // Expected output: "Not Equal"
    }

    try {
        console.log(expect(5).notToBe(null)); // Expected output: true
    } catch (error) {
        console.error(error.message);
    }

    try {
        console.log(expect("hello").toBe("hello")); // Expected output: true
    } catch (error) {
        console.error(error.message);
    }

    try {
        console.log(expect("hello").notToBe("world")); // Expected output: true
    } catch (error) {
        console.error(error.message);
    }

    try {
        console.log(expect(true).toBe(true)); // Expected output: true
    } catch (error) {
        console.error(error.message);
    }

    try {
        console.log(expect(false).notToBe(true)); // Expected output: true
    } catch (error) {
        console.error(error.message);
    }
}

/*

Complexity Analysis:
- Time Complexity: O(1) - Each function call performs a single comparison, which is constant time.
- Space Complexity: O(1) - No additional memory is allocated apart from the returned object.

*/


