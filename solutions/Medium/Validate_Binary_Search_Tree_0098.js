/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val);
 *     this.left = (left===undefined ? null : left);
 *     this.right = (right===undefined ? null : right);
 * }
 */

/**
 * Function: isValidBST
 * Description: Given the root of a binary tree, this function determines if the tree is a 
 * valid binary search tree (BST). A BST must satisfy:
 * - Left subtree nodes must have values < current node.
 * - Right subtree nodes must have values > current node.
 * - Both subtrees must also be valid BSTs.
 *
 * @param {TreeNode} root - The root node of the binary tree.
 * @returns {boolean} - True if the tree is a valid BST, otherwise false.
 */
const isValidBST = function(root) {
    /**
     * Helper function to validate BST using min and max constraints.
     * @param {TreeNode} node - The current node being checked.
     * @param {number} min - Minimum allowable value for this node.
     * @param {number} max - Maximum allowable value for this node.
     * @returns {boolean} - True if valid BST, false otherwise.
     */
    const validate = (node, min, max) => {
        if (!node) return true; // Base case: null nodes are valid

        // Check if current node value violates BST constraints
        if (node.val <= min || node.val >= max) return false;

        // Recursively validate left and right subtrees with updated constraints
        return validate(node.left, min, node.val) && validate(node.right, node.val, max);
    };

    return validate(root, -Infinity, Infinity);
};

// Example Test Cases
if (require.main === module) {
    const TreeNode = function(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    };

    console.log("Test 1: Valid BST");
    let root1 = new TreeNode(2, new TreeNode(1), new TreeNode(3));
    console.log(isValidBST(root1));
    // Expected output: true

    console.log("Test 2: Invalid BST with wrong right child");
    let root2 = new TreeNode(5, 
        new TreeNode(1), 
        new TreeNode(4, new TreeNode(3), new TreeNode(6))
    );
    console.log(isValidBST(root2));
    // Expected output: false

    console.log("Test 3: Single node tree");
    let root3 = new TreeNode(10);
    console.log(isValidBST(root3));
    // Expected output: true

    console.log("Test 4: Large valid BST");
    let root4 = new TreeNode(10, 
        new TreeNode(5, new TreeNode(2), new TreeNode(7)), 
        new TreeNode(15, new TreeNode(12), new TreeNode(20))
    );
    console.log(isValidBST(root4));
    // Expected output: true

    console.log("Test 5: Invalid BST with left child greater than root");
    let root5 = new TreeNode(10, new TreeNode(12), new TreeNode(15));
    console.log(isValidBST(root5));
    // Expected output: false

    console.log("Test 6: Invalid BST with right subtree having smaller node");
    let root6 = new TreeNode(10, 
        new TreeNode(5, new TreeNode(2), new TreeNode(7)), 
        new TreeNode(15, new TreeNode(6), new TreeNode(20))
    );
    console.log(isValidBST(root6));
    // Expected output: false
}

/*
Time Complexity: O(n) - Each node is visited once.
Space Complexity: O(h) - Recursion stack depth (O(log n) for balanced, O(n) for skewed trees).
*/

export default isValidBST;
