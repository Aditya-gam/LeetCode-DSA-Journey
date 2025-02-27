/**
 * Function: permute
 * Description: Given an array of distinct integers `nums`, this function returns all possible 
 * permutations of the elements.
 *
 * @param {number[]} nums - An array of distinct integers.
 * @returns {number[][]} - A list containing all permutations of `nums`.
 */
const permute = function(nums) {
    let result = [];

    /**
     * Backtracking function to generate permutations.
     * @param {number[]} current - The current permutation being formed.
     * @param {boolean[]} used - Boolean array to track used elements.
     */
    const backtrack = (current, used) => {
        // If current permutation has all numbers, add it to result
        if (current.length === nums.length) {
            result.push([...current]);
            return;
        }

        // Iterate through nums and construct permutations
        for (let i = 0; i < nums.length; i++) {
            if (used[i]) continue; // Skip already used numbers

            used[i] = true; // Mark current number as used
            current.push(nums[i]); // Add number to the current permutation
            backtrack(current, used); // Recurse with updated state
            current.pop(); // Backtrack: remove last number
            used[i] = false; // Reset used flag
        }
    };

    // Start backtracking with an empty permutation
    backtrack([], new Array(nums.length).fill(false));

    return result;
};

// Example Test Cases
if (require.main === module) {
    console.log("Test 1: Basic case with three numbers");
    console.log(permute([1, 2, 3]));
    // Expected output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    console.log("Test 2: Case with two numbers");
    console.log(permute([0, 1]));
    // Expected output: [[0,1],[1,0]]

    console.log("Test 3: Single number case");
    console.log(permute([1]));
    // Expected output: [[1]]

    console.log("Test 4: Case with four numbers");
    console.log(permute([1, 2, 3, 4]));
    // Expected output: 24 unique permutations

    console.log("Test 5: Case with negative numbers");
    console.log(permute([-1, 2, -3]));
    // Expected output: All possible orders of [-1,2,-3]

    console.log("Test 6: Case with the largest input (6 numbers)");
    console.log(permute([1, 2, 3, 4, 5, 6]).length);
    // Expected output: 6! = 720
}

/* Complexity analysis:
Time Complexity: O(n!) - There are n! permutations for an array of size n.
Space Complexity: O(n!) - Due to storing all permutations in the result array.
*/

export default permute;
