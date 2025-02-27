/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val);
 *     this.left = (left===undefined ? null : left);
 *     this.right = (right===undefined ? null : right);
 * }
 */

/**
 * Function: inorderTraversal (Recursive)
 * Description: Given the root of a binary tree, this function returns an array containing 
 * the inorder traversal of the tree's nodes' values using recursion.
 *
 * @param {TreeNode} root - The root node of the binary tree.
 * @returns {number[]} - The inorder traversal of the tree.
 */
const inorderTraversalRecursive = function(root) {
    let result = [];

    /**
     * Helper function for recursive traversal.
     * @param {TreeNode} node - The current node.
     */
    const inorder = (node) => {
        if (!node) return;
        inorder(node.left);     // Traverse left subtree
        result.push(node.val);  // Visit the node
        inorder(node.right);    // Traverse right subtree
    };

    inorder(root);
    
    return result;
};

/**
 * Function: inorderTraversal (Iterative)
 * Description: Given the root of a binary tree, this function returns an array containing 
 * the inorder traversal of the tree's nodes' values using an iterative approach.
 *
 * @param {TreeNode} root - The root node of the binary tree.
 * @returns {number[]} - The inorder traversal of the tree.
 */
const inorderTraversalIterative = function(root) {
    let result = [];
    let stack = [];
    let current = root;

    while (current !== null || stack.length > 0) {
        // Reach the leftmost node of the current node
        while (current !== null) {
            stack.push(current);
            current = current.left;
        }

        // Current must be null at this point, so we pop from the stack
        current = stack.pop();
        result.push(current.val); // Visit the node

        // Move to the right subtree
        current = current.right;
    }

    return result;
};

// Example Test Cases
if (require.main === module) {
    const TreeNode = function(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    };

    console.log("Test 1: Basic tree with right child");
    let root1 = new TreeNode(1, null, new TreeNode(2, new TreeNode(3)));
    console.log(inorderTraversalRecursive(root1)); // Expected output: [1,3,2]
    console.log(inorderTraversalIterative(root1)); // Expected output: [1,3,2]

    console.log("Test 2: Complex tree");
    let root2 = new TreeNode(1,
        new TreeNode(2, new TreeNode(4), new TreeNode(5, new TreeNode(6), new TreeNode(7))),
        new TreeNode(3, null, new TreeNode(8, new TreeNode(9)))
    );
    console.log(inorderTraversalRecursive(root2)); // Expected: [4,2,6,5,7,1,3,9,8]
    console.log(inorderTraversalIterative(root2)); // Expected: [4,2,6,5,7,1,3,9,8]

    console.log("Test 3: Empty tree");
    console.log(inorderTraversalRecursive(null)); // Expected: []
    console.log(inorderTraversalIterative(null)); // Expected: []

    console.log("Test 4: Single node tree");
    let root3 = new TreeNode(1);
    console.log(inorderTraversalRecursive(root3)); // Expected: [1]
    console.log(inorderTraversalIterative(root3)); // Expected: [1]

    console.log("Test 5: Left skewed tree");
    let root4 = new TreeNode(5, new TreeNode(4, new TreeNode(3, new TreeNode(2, new TreeNode(1)))));
    console.log(inorderTraversalRecursive(root4)); // Expected: [1,2,3,4,5]
    console.log(inorderTraversalIterative(root4)); // Expected: [1,2,3,4,5]

    console.log("Test 6: Right skewed tree");
    let root5 = new TreeNode(1, null, new TreeNode(2, null, new TreeNode(3, null, new TreeNode(4, null, new TreeNode(5)))));
    console.log(inorderTraversalRecursive(root5)); // Expected: [1,2,3,4,5]
    console.log(inorderTraversalIterative(root5)); // Expected: [1,2,3,4,5]
}

/*
Time Complexity:
- Recursive: O(n) - Visits each node once.
- Iterative: O(n) - Each node is processed once.

Space Complexity:
- Recursive: O(h) - Stack depth is the height of the tree (O(log n) for balanced, O(n) for skewed).
- Iterative: O(h) - Stack stores nodes up to the height of the tree.
*/

export default inorderTraversalRecursive;
export { inorderTraversalIterative };