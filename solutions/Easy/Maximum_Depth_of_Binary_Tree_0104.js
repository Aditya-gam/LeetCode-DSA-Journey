/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val);
 *     this.left = (left===undefined ? null : left);
 *     this.right = (right===undefined ? null : right);
 * }
 */

/**
 * Function: maxDepth (Recursive DFS)
 * Description: Given the root of a binary tree, this function returns its maximum depth.
 * The maximum depth is the longest path from the root to a leaf node.
 *
 * @param {TreeNode} root - The root node of the binary tree.
 * @returns {number} - The maximum depth of the tree.
 */
const maxDepth = function(root) {
    if (!root) return 0; // Base case: If tree is empty, depth is 0
    
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
};

/**
 * Function: maxDepthIterative (BFS Approach)
 * Description: This function finds the maximum depth using level-order traversal (BFS).
 *
 * @param {TreeNode} root - The root node of the binary tree.
 * @returns {number} - The maximum depth of the tree.
 */
const maxDepthIterative = function(root) {
    if (!root) return 0; // Base case: Empty tree has depth 0

    let queue = [root];
    let depth = 0;

    while (queue.length > 0) {
        let levelSize = queue.length;
        depth++;

        for (let i = 0; i < levelSize; i++) {
            let currentNode = queue.shift();

            if (currentNode.left) queue.push(currentNode.left);
            if (currentNode.right) queue.push(currentNode.right);
        }
    }

    return depth;
};

// Example Test Cases
if (require.main === module) {
    const TreeNode = function(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    };

    console.log("Test 1: Balanced binary tree");
    let root1 = new TreeNode(3, 
        new TreeNode(9), 
        new TreeNode(20, new TreeNode(15), new TreeNode(7))
    );
    console.log(maxDepth(root1)); // Expected output: 3
    console.log(maxDepthIterative(root1)); // Expected output: 3

    console.log("Test 2: Right-skewed tree");
    let root2 = new TreeNode(1, null, new TreeNode(2));
    console.log(maxDepth(root2)); // Expected output: 2
    console.log(maxDepthIterative(root2)); // Expected output: 2

    console.log("Test 3: Empty tree");
    console.log(maxDepth(null)); // Expected output: 0
    console.log(maxDepthIterative(null)); // Expected output: 0

    console.log("Test 4: Single node tree");
    let root3 = new TreeNode(5);
    console.log(maxDepth(root3)); // Expected output: 1
    console.log(maxDepthIterative(root3)); // Expected output: 1

    console.log("Test 5: Left-skewed tree");
    let root4 = new TreeNode(1, new TreeNode(2, new TreeNode(3, new TreeNode(4, new TreeNode(5)))));
    console.log(maxDepth(root4)); // Expected output: 5
    console.log(maxDepthIterative(root4)); // Expected output: 5

    console.log("Test 6: Larger tree with mixed structure");
    let root5 = new TreeNode(10, 
        new TreeNode(5, new TreeNode(2), new TreeNode(7)), 
        new TreeNode(15, new TreeNode(12), new TreeNode(20))
    );
    console.log(maxDepth(root5)); // Expected output: 3
    console.log(maxDepthIterative(root5)); // Expected output: 3
}

/*
Time Complexity:
- Recursive DFS: O(n) - Each node is visited once.
- Iterative BFS: O(n) - Each node is processed level by level.

Space Complexity:
- Recursive DFS: O(h) - Recursion depth (O(log n) for balanced, O(n) for skewed trees).
- Iterative BFS: O(n) - Queue stores nodes level-wise.
*/

export { maxDepth, maxDepthIterative };
