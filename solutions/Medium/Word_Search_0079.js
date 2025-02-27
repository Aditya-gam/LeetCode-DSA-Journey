/**
 * Function: exist
 * Description: Given an `m x n` grid of characters `board` and a string `word`, this function 
 * determines whether the word exists in the grid. The word must be formed by sequentially 
 * adjacent cells (horizontally or vertically), and a cell cannot be used more than once.
 *
 * @param {character[][]} board - The `m x n` grid of characters.
 * @param {string} word - The target word to search in the board.
 * @returns {boolean} - `true` if the word exists, otherwise `false`.
 */
const exist = function(board, word) {
    let rows = board.length, cols = board[0].length;

    /**
     * Backtracking function to explore all possible paths.
     * @param {number} r - Current row index.
     * @param {number} c - Current column index.
     * @param {number} index - Current position in `word`.
     * @returns {boolean} - True if the word is found.
     */
    const backtrack = (r, c, index) => {
        // If we reach the end of the word, return true
        if (index === word.length) return true;

        // Boundary conditions and character match check
        if (r < 0 || c < 0 || r >= rows || c >= cols || board[r][c] !== word[index]) return false;

        // Mark the current cell as visited by replacing it with a placeholder
        let temp = board[r][c];
        board[r][c] = "#"; // Mark as visited

        // Explore all possible directions (right, left, down, up)
        let found = backtrack(r + 1, c, index + 1) || 
                    backtrack(r - 1, c, index + 1) || 
                    backtrack(r, c + 1, index + 1) || 
                    backtrack(r, c - 1, index + 1);

        // Restore the original value for backtracking
        board[r][c] = temp;

        return found;
    };

    // Iterate through each cell in the grid as a starting point
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (backtrack(r, c, 0)) return true; // Start backtracking if the first letter matches
        }
    }

    return false;
};

// Example Test Cases
if (require.main === module) {
    console.log("Test 1: Word exists in the board");
    console.log(exist([
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ], "ABCCED"));
    // Expected output: true

    console.log("Test 2: Another valid word in the board");
    console.log(exist([
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ], "SEE"));
    // Expected output: true

    console.log("Test 3: Word cannot be formed");
    console.log(exist([
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ], "ABCB"));
    // Expected output: false

    console.log("Test 4: Single letter grid matching the word");
    console.log(exist([
        ["A"]
    ], "A"));
    // Expected output: true

    console.log("Test 5: Single letter grid not matching the word");
    console.log(exist([
        ["B"]
    ], "A"));
    // Expected output: false

    console.log("Test 6: Large grid with complex path");
    console.log(exist([
        ["C","A","A"],
        ["A","A","A"],
        ["B","C","D"]
    ], "AAB"));
    // Expected output: true
}

/*
Time Complexity: O(m * n * 4^k) - Worst case explores all 4 directions for each letter in `word`.
Space Complexity: O(k) - Due to recursion depth of `k` (length of `word`).
*/

export default exist;
