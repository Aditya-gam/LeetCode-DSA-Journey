/**
 * Function: combinationSum
 * Description: Given an array of distinct integers `candidates` and a target integer `target`,
 * this function returns all unique combinations of numbers that sum to `target`. 
 * Each number in `candidates` may be used an unlimited number of times.
 *
 * @param {number[]} candidates - An array of distinct positive integers.
 * @param {number} target - The target sum to achieve.
 * @returns {number[][]} - A list of all unique combinations summing to `target`.
 */
const combinationSum = function(candidates, target) {
    let result = [];

    /**
     * Backtracking function to find valid combinations.
     * @param {number} start - The current index in the `candidates` array.
     * @param {number[]} combination - The current combination of numbers.
     * @param {number} sum - The current sum of elements in `combination`.
     */
    const backtrack = (start, combination, sum) => {
        // If sum equals target, add the combination to the result
        if (sum === target) {
            result.push([...combination]);
            return;
        }

        // If sum exceeds target, stop exploring further
        if (sum > target) return;

        // Iterate over the candidates starting from `start` index
        for (let i = start; i < candidates.length; i++) {
            combination.push(candidates[i]); // Include the current candidate
            backtrack(i, combination, sum + candidates[i]); // Recur with the same index (unlimited reuse)
            combination.pop(); // Backtrack and remove the last added element
        }
    };

    // Start backtracking with an empty combination
    backtrack(0, [], 0);

    return result;
};

// Example Test Cases
if (require.main === module) {
    console.log("Test 1: Basic case");
    console.log(combinationSum([2, 3, 6, 7], 7));
    // Expected output: [[2,2,3],[7]]

    console.log("Test 2: Multiple valid combinations");
    console.log(combinationSum([2, 3, 5], 8));
    // Expected output: [[2,2,2,2],[2,3,3],[3,5]]

    console.log("Test 3: No valid combinations");
    console.log(combinationSum([2], 1));
    // Expected output: []

    console.log("Test 4: Single candidate can form target multiple ways");
    console.log(combinationSum([3], 9));
    // Expected output: [[3,3,3]]

    console.log("Test 5: Large target with different numbers");
    console.log(combinationSum([2, 5, 10], 20));
    // Expected output: [[2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,5],[2,2,2,2,2,2,5,5],[2,2,2,2,5,5,5],[2,2,2,10,10],[2,2,5,5,5,5],[2,5,5,5,5],[5,5,5,5],[10,10]]

    console.log("Test 6: Only one candidate and it's exactly target");
    console.log(combinationSum([7], 7));
    // Expected output: [[7]]
}

// Complexity analysis
// Time Complexity: O(2^n) - Exponential due to generating all possible subsets.
// Space Complexity: O(2^n) - Due to storing all valid subsets in the result array.

export default combinationSum;