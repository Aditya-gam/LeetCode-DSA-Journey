/**
 * Function: subsets
 * Description: Given an integer array `nums` of unique elements, this function returns 
 * all possible subsets (the power set) of `nums`.
 *
 * @param {number[]} nums - An array of unique integers.
 * @returns {number[][]} - A list containing all possible subsets.
 */
const subsets = function(nums) {
    let result = [];

    /**
     * Backtracking function to generate subsets.
     * @param {number} index - The current index in `nums`.
     * @param {number[]} current - The current subset being formed.
     */
    const backtrack = (index, current) => {
        // Add the current subset to the result
        result.push([...current]);

        // Iterate through all possible elements starting from `index`
        for (let i = index; i < nums.length; i++) {
            current.push(nums[i]); // Include element in subset
            backtrack(i + 1, current); // Recurse with the next index
            current.pop(); // Backtrack: Remove the last element
        }
    };

    // Start backtracking with an empty subset
    backtrack(0, []);

    return result;
};

// Example Test Cases
if (require.main === module) {
    console.log("Test 1: Basic case with three numbers");
    console.log(subsets([1, 2, 3]));
    // Expected output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    console.log("Test 2: Case with single number");
    console.log(subsets([0]));
    // Expected output: [[],[0]]

    console.log("Test 3: Case with four numbers");
    console.log(subsets([1, 2, 3, 4]));
    // Expected output: 16 subsets (2^4)

    console.log("Test 4: Case with negative numbers");
    console.log(subsets([-1, 2, -3]));
    // Expected output: Power set of [-1, 2, -3]

    console.log("Test 5: Case with maximum input size (10 numbers)");
    console.log(subsets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).length);
    // Expected output: 2^10 = 1024

    console.log("Test 6: Case with two numbers");
    console.log(subsets([5, 7]));
    // Expected output: [[], [5], [7], [5,7]]
}

/*
Time Complexity: O(2^n) - Each element can either be included or excluded, leading to 2^n subsets.
Space Complexity: O(2^n) - The result array stores all subsets.
*/

export default subsets;