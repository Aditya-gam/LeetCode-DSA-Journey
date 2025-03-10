/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val);
 *     this.left = (left===undefined ? null : left);
 *     this.right = (right===undefined ? null : right);
 * }
 */

/**
 * Function: maxPathSum
 * Description: Given the root of a binary tree, this function returns the maximum path sum
 * for any path in the tree. A path consists of nodes connected by edges, and each node 
 * can only appear once in a path.
 *
 * @param {TreeNode} root - The root of the binary tree.
 * @returns {number} - The maximum path sum of any non-empty path.
 */
const maxPathSum = function(root) {
    let maxSum = -Infinity;

    /**
     * Helper function to compute maximum path sum for each subtree.
     * @param {TreeNode} node - The current node.
     * @returns {number} - Maximum path sum including this node.
     */
    const maxGain = (node) => {
        if (!node) return 0;

        // Compute max sum on the left and right; discard negatives (max with 0)
        let leftGain = Math.max(maxGain(node.left), 0);
        let rightGain = Math.max(maxGain(node.right), 0);

        // Compute max path sum where current node is the highest node (split path)
        let pathSum = node.val + leftGain + rightGain;

        // Update max sum found
        maxSum = Math.max(maxSum, pathSum);

        // Return max gain from this node (choosing either left or right)
        return node.val + Math.max(leftGain, rightGain);
    };

    maxGain(root);
    
    return maxSum;
};

// Example Test Cases
if (require.main === module) {
    const TreeNode = function(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    };

    console.log("Test 1: Basic case with root = [1,2,3]");
    let root1 = new TreeNode(1, new TreeNode(2), new TreeNode(3));
    console.log(maxPathSum(root1));
    // Expected output: 6 (Path: 2 -> 1 -> 3)

    console.log("Test 2: More complex tree");
    let root2 = new TreeNode(-10, 
        new TreeNode(9), 
        new TreeNode(20, new TreeNode(15), new TreeNode(7))
    );
    console.log(maxPathSum(root2));
    // Expected output: 42 (Path: 15 -> 20 -> 7)

    console.log("Test 3: Single node tree");
    let root3 = new TreeNode(5);
    console.log(maxPathSum(root3));
    // Expected output: 5

    console.log("Test 4: Tree with all negative values");
    let root4 = new TreeNode(-3, new TreeNode(-2), new TreeNode(-1));
    console.log(maxPathSum(root4));
    // Expected output: -1 (Max single node)

    console.log("Test 5: Tree with zero values");
    let root5 = new TreeNode(0, new TreeNode(-2), new TreeNode(3));
    console.log(maxPathSum(root5));
    // Expected output: 3 (Choosing the right child only)

    console.log("Test 6: Unbalanced tree");
    let root6 = new TreeNode(1, new TreeNode(2, new TreeNode(3, new TreeNode(4))), null);
    console.log(maxPathSum(root6));
    // Expected output: 10 (Path: 4 -> 3 -> 2 -> 1)
}

/*
Time Complexity: O(n) - Visits each node once.
Space Complexity: O(h) - Recursion depth equals the tree height (O(log n) for balanced trees, O(n) for skewed trees).
*/

export default maxPathSum;
