/**
 * Class: ArrayWrapper
 * Description: This class wraps an array and provides custom behavior for:
 * - `+` operator: Returns the sum of all elements when instances are added together.
 * - `String()` function: Returns a comma-separated string in bracket notation.
 */
class ArrayWrapper {
    /**
     * Constructor initializes the instance with an array of numbers.
     * @param {number[]} nums - The array of numbers to wrap.
     */
    constructor(nums) {
        this.nums = nums;
    }

    /**
     * Function: valueOf
     * Description: Returns the sum of all elements in the wrapped array.
     * This allows `+` operator to sum two ArrayWrapper instances.
     *
     * @return {number} - The sum of elements.
     */
    valueOf() {
        return this.nums.reduce((sum, num) => sum + num, 0);
    }

    /**
     * Function: toString
     * Description: Returns the string representation of the array in `[1,2,3]` format.
     *
     * @return {string} - String representation of the array.
     */
    toString() {
        return `[${this.nums.join(",")}]`;
    }
}

// Example Test Cases
if (require.main === module) {
    const obj1 = new ArrayWrapper([1, 2]);
    const obj2 = new ArrayWrapper([3, 4]);

    console.log(obj1 + obj2);
    // Expected output: 10

    console.log(String(obj1));
    // Expected output: "[1,2]"

    console.log(String(obj2));
    // Expected output: "[3,4]"

    const obj3 = new ArrayWrapper([]);
    const obj4 = new ArrayWrapper([]);
    
    console.log(obj3 + obj4);
    // Expected output: 0

    console.log(String(obj3));
    // Expected output: "[]"

    console.log(String(new ArrayWrapper([23, 98, 42, 70])));
    // Expected output: "[23,98,42,70]"
}

/*

Complexity Analysis:
- Time Complexity:
  - `valueOf()`: O(n), as it iterates over the array to compute the sum.
  - `toString()`: O(n), as it joins array elements into a string.
- Space Complexity: O(1), as it only stores a reference to the input array.

*/

export default ArrayWrapper;
