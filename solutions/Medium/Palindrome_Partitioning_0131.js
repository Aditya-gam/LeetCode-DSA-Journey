/**
 * Function: partition
 * Description: Given a string `s`, this function returns all possible ways to partition `s`
 * such that every substring in the partition is a palindrome.
 *
 * @param {string} s - The input string containing only lowercase letters.
 * @returns {string[][]} - A list containing all valid palindrome partitions.
 */
const partition = function(s) {
    let result = [];

    /**
     * Helper function to check if a substring is a palindrome.
     * @param {string} str - The substring to check.
     * @returns {boolean} - True if the substring is a palindrome.
     */
    const isPalindrome = (str) => {
        let left = 0, right = str.length - 1;
        while (left < right) {
            if (str[left] !== str[right]) return false;
            left++;
            right--;
        }
        return true;
    };

    /**
     * Backtracking function to generate palindrome partitions.
     * @param {number} start - The starting index for the current partition.
     * @param {string[]} current - The current partition being formed.
     */
    const backtrack = (start, current) => {
        if (start === s.length) {
            result.push([...current]);
            return;
        }

        for (let end = start + 1; end <= s.length; end++) {
            let substring = s.slice(start, end);
            if (isPalindrome(substring)) {
                current.push(substring);
                backtrack(end, current);
                current.pop(); // Backtrack
            }
        }
    };

    // Start backtracking from index 0
    backtrack(0, []);

    return result;
};

// Example Test Cases
if (require.main === module) {
    console.log("Test 1: Basic case with s = 'aab'");
    console.log(partition("aab"));
    // Expected output: [["a","a","b"],["aa","b"]]

    console.log("Test 2: Single character string");
    console.log(partition("a"));
    // Expected output: [["a"]]

    console.log("Test 3: String with all characters the same");
    console.log(partition("aaa"));
    // Expected output: [["a","a","a"],["a","aa"],["aa","a"],["aaa"]]

    console.log("Test 4: String with no palindromes larger than 1");
    console.log(partition("abc"));
    // Expected output: [["a","b","c"]]

    console.log("Test 5: String with mixed palindromes");
    console.log(partition("racecar"));
    // Expected output: [["r","a","c","e","c","a","r"],["r","a","cec","a","r"],["r","aceca","r"],["racecar"]]

    console.log("Test 6: Edge case with maximum length input (16 characters)");
    console.log(partition("aaaaaaaaaaaaaaaa").length);
    // Expected output: Large number of partitions
}

/*
Time Complexity: O(2^n) - Each character has the option to either start a new partition or continue an existing one.
Space Complexity: O(n) - Due to the recursion depth and storing partitions.
*/

export default partition;
