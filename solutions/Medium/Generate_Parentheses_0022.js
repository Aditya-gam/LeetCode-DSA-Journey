/**
 * Function: generateParenthesis
 * Description: Given `n` pairs of parentheses, this function generates all possible 
 * well-formed combinations using backtracking.
 *
 * @param {number} n - Number of pairs of parentheses.
 * @returns {string[]} - An array containing all valid combinations of parentheses.
 */
const generateParenthesis = function(n) {
    let result = [];

    /**
     * Backtracking function to generate valid parentheses combinations.
     * @param {string} combination - The current combination being formed.
     * @param {number} open - Number of open parentheses used.
     * @param {number} close - Number of closed parentheses used.
     */
    const backtrack = (combination, open, close) => {
        // If the combination reaches the required length, add it to the result
        if (combination.length === 2 * n) {
            result.push(combination);
            return;
        }

        // Add an open parenthesis if it does not exceed `n`
        if (open < n) {
            backtrack(combination + "(", open + 1, close);
        }

        // Add a close parenthesis if it does not exceed the open count
        if (close < open) {
            backtrack(combination + ")", open, close + 1);
        }
    };

    // Start the backtracking process with an empty string
    backtrack("", 0, 0);

    return result;
};

// Example Test Cases
if (require.main === module) {
    console.log("Test 1: Basic case with n = 3");
    console.log(generateParenthesis(3));
    // Expected output: ["((()))","(()())","(())()","()(())","()()()"]

    console.log("Test 2: Smallest case with n = 1");
    console.log(generateParenthesis(1));
    // Expected output: ["()"]

    console.log("Test 3: Case with n = 2");
    console.log(generateParenthesis(2));
    // Expected output: ["(())", "()()"]

    console.log("Test 4: Edge case with maximum n = 8 (should generate 1430 valid combinations)");
    console.log(generateParenthesis(8).length);
    // Expected output: 1430

    console.log("Test 5: Case with n = 4");
    console.log(generateParenthesis(4));
    // Expected output: ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]

    console.log("Test 6: Case with n = 5");
    console.log(generateParenthesis(5).length);
    // Expected output: 42 (Number of valid combinations for n = 5)
}

//  Complexity analysis
// Time Complexity: O(4^n / sqrt(n)) - This is the Catalan number growth rate.
// Space Complexity: O(4^n / sqrt(n)) - Due to storing all valid combinations in the result array.

export default generateParenthesis;