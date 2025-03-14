/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val);
 *     this.left = (left===undefined ? null : left);
 *     this.right = (right===undefined ? null : right);
 * }
 */

/**
 * Function: isSymmetric (Recursive Approach)
 * Description: Given the root of a binary tree, this function checks if the tree is 
 * symmetric (a mirror image of itself) using recursion.
 *
 * @param {TreeNode} root - The root node of the binary tree.
 * @returns {boolean} - True if the tree is symmetric, otherwise false.
 */
const isSymmetric = function(root) {
    if (!root) return true;

    /**
     * Helper function to check if two subtrees are mirror images.
     * @param {TreeNode} left - Left subtree.
     * @param {TreeNode} right - Right subtree.
     * @returns {boolean} - True if they are mirror images, otherwise false.
     */
    const isMirror = (left, right) => {
        if (!left && !right) return true; // Both nodes are null
        if (!left || !right) return false; // One is null, but not the other
        if (left.val !== right.val) return false; // Values don't match

        // Check symmetry in subtrees: left's left with right's right and left's right with right's left
        return isMirror(left.left, right.right) && isMirror(left.right, right.left);
    };

    return isMirror(root.left, root.right);
};

/**
 * Function: isSymmetricIterative (Iterative Approach)
 * Description: Uses BFS (queue) to check for symmetry in a binary tree.
 *
 * @param {TreeNode} root - The root node of the binary tree.
 * @returns {boolean} - True if the tree is symmetric, otherwise false.
 */
const isSymmetricIterative = function(root) {
    if (!root) return true;

    let queue = [[root.left, root.right]];

    while (queue.length > 0) {
        let [left, right] = queue.shift();

        if (!left && !right) continue; // Both null, continue checking
        if (!left || !right || left.val !== right.val) return false; // One null or values mismatch

        // Enqueue pairs to check symmetry
        queue.push([left.left, right.right]); // Outer symmetry
        queue.push([left.right, right.left]); // Inner symmetry
    }

    return true;
};

// Example Test Cases
if (require.main === module) {
    const TreeNode = function(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    };

    console.log("Test 1: Symmetric tree");
    let root1 = new TreeNode(1, 
        new TreeNode(2, new TreeNode(3), new TreeNode(4)), 
        new TreeNode(2, new TreeNode(4), new TreeNode(3))
    );
    console.log(isSymmetric(root1)); // Expected output: true
    console.log(isSymmetricIterative(root1)); // Expected output: true

    console.log("Test 2: Asymmetric tree");
    let root2 = new TreeNode(1, 
        new TreeNode(2, null, new TreeNode(3)), 
        new TreeNode(2, null, new TreeNode(3))
    );
    console.log(isSymmetric(root2)); // Expected output: false
    console.log(isSymmetricIterative(root2)); // Expected output: false

    console.log("Test 3: Single node tree");
    let root3 = new TreeNode(1);
    console.log(isSymmetric(root3)); // Expected output: true
    console.log(isSymmetricIterative(root3)); // Expected output: true

    console.log("Test 4: Left-skewed tree");
    let root4 = new TreeNode(1, new TreeNode(2, new TreeNode(3)));
    console.log(isSymmetric(root4)); // Expected output: false
    console.log(isSymmetricIterative(root4)); // Expected output: false

    console.log("Test 5: Right-skewed tree");
    let root5 = new TreeNode(1, null, new TreeNode(2, null, new TreeNode(3)));
    console.log(isSymmetric(root5)); // Expected output: false
    console.log(isSymmetricIterative(root5)); // Expected output: false

    console.log("Test 6: Empty tree");
    console.log(isSymmetric(null)); // Expected output: true
    console.log(isSymmetricIterative(null)); // Expected output: true
}

/*
Time Complexity:
- Recursive: O(n) - Each node is visited once.
- Iterative: O(n) - Each node is processed once.

Space Complexity:
- Recursive: O(h) - Recursion depth (O(log n) for balanced, O(n) for skewed trees).
- Iterative: O(n) - Queue stores nodes level-wise.
*/

export { isSymmetric, isSymmetricIterative };
