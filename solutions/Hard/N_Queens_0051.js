/**
 * Function: solveNQueens
 * Description: Given an integer `n`, this function returns all distinct solutions 
 * for placing `n` queens on an `n x n` chessboard such that no two queens attack each other.
 *
 * @param {number} n - The size of the chessboard (n x n).
 * @returns {string[][]} - A list of valid board configurations.
 */
const solveNQueens = function(n) {
    let results = [];

    /**
     * Backtracking function to place queens on the board.
     * @param {number} row - The current row to place a queen.
     * @param {number[]} columns - Column positions of placed queens.
     * @param {Set} diagonals - Set tracking occupied diagonals (`row - col`).
     * @param {Set} antiDiagonals - Set tracking occupied anti-diagonals (`row + col`).
     */
    const backtrack = (row, columns, diagonals, antiDiagonals) => {
        if (row === n) {
            results.push(generateBoard(columns, n));
            return;
        }

        for (let col = 0; col < n; col++) {
            if (columns.includes(col) || diagonals.has(row - col) || antiDiagonals.has(row + col)) continue;

            // Place queen
            columns.push(col);
            diagonals.add(row - col);
            antiDiagonals.add(row + col);

            // Recurse to next row
            backtrack(row + 1, columns, diagonals, antiDiagonals);

            // Backtrack: Remove the queen
            columns.pop();
            diagonals.delete(row - col);
            antiDiagonals.delete(row + col);
        }
    };

    /**
     * Function to generate board representation from column positions.
     * @param {number[]} columns - The column indices of the queens.
     * @param {number} n - The size of the board.
     * @returns {string[]} - The board representation.
     */
    const generateBoard = (columns, n) => {
        return columns.map(col => ".".repeat(col) + "Q" + ".".repeat(n - col - 1));
    };

    // Start backtracking from row 0
    backtrack(0, [], new Set(), new Set());

    return results;
};

// Example Test Cases
if (require.main === module) {
    console.log("Test 1: Basic case with n = 4");
    console.log(solveNQueens(4));
    // Expected output: Two distinct solutions.

    console.log("Test 2: Smallest case with n = 1");
    console.log(solveNQueens(1));
    // Expected output: [["Q"]]

    console.log("Test 3: Case with n = 2 (No solutions)");
    console.log(solveNQueens(2));
    // Expected output: []

    console.log("Test 4: Case with n = 3 (No solutions)");
    console.log(solveNQueens(3));
    // Expected output: []

    console.log("Test 5: Case with n = 5");
    console.log(solveNQueens(5).length);
    // Expected output: 10 unique solutions.

    console.log("Test 6: Case with n = 6");
    console.log(solveNQueens(6).length);
    // Expected output: 4 unique solutions.
}

/* Complexity analysis:
Time Complexity: O(n!) - The backtracking explores all possible placements.
Space Complexity: O(n) - Stores column indices, diagonals, and anti-diagonals.
*/

export default solveNQueens;
