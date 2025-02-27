/**
 * Function: letterCombinations
 * Description: Given a string of digits from 2-9, this function returns all possible letter 
 * combinations that the number could represent based on the telephone keypad mapping.
 *
 * @param {string} digits - A string containing digits from '2' to '9'.
 * @returns {string[]} - An array of all possible letter combinations.
 */
const letterCombinations = function(digits) {
    if (!digits.length) return []; // Return an empty array if input is empty.

    // Mapping of digits to corresponding letters on a telephone keypad.
    const digitToLetters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    };

    let result = [];

    /**
     * Backtracking helper function to generate all letter combinations.
     * @param {string} combination - Current string combination being built.
     * @param {number} index - Current index in the digits string.
     */
    const backtrack = (combination, index) => {
        // If combination length matches digits length, add to result.
        if (index === digits.length) {
            result.push(combination);
            return;
        }

        // Retrieve the corresponding letters for the current digit.
        let letters = digitToLetters[digits[index]];
        for (let letter of letters) {
            backtrack(combination + letter, index + 1);
        }
    };

    // Start the backtracking process.
    backtrack("", 0);

    return result;
};

// Example Test Cases
if (require.main === module) {
    console.log("Test 1: Basic case with two digits");
    console.log(letterCombinations("23"));
    // Expected output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    console.log("Test 2: Edge case - empty input");
    console.log(letterCombinations(""));
    // Expected output: []

    console.log("Test 3: Single digit input");
    console.log(letterCombinations("2"));
    // Expected output: ["a", "b", "c"]

    console.log("Test 4: Two-digit input with four-letter mappings");
    console.log(letterCombinations("79"));
    // Expected output: ["pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]

    console.log("Test 5: Three-digit input");
    console.log(letterCombinations("345"));
    // Expected output: 27 combinations of 'd', 'e', 'f' with 'g', 'h', 'i' with 'j', 'k', 'l'

    console.log("Test 6: Four-digit input (maximum allowed)");
    console.log(letterCombinations("6789"));
    // Expected output: 3x3x4x4 = 144 combinations
}

// Complexity Analysis
// Time Complexity: O(4^n) - Each digit has 3 or 4 letters leading to exponential growth.
// Space Complexity: O(4^n) - Stores all combinations in the result array.

export default letterCombinations;
