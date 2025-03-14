/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * Function: rightSideView
 * Description: This function returns the values of the nodes visible when looking at a binary tree from the right side.
 * - Uses a level-order traversal (BFS) to collect the last node of each level.
 *
 * @param {TreeNode} root - The root of the binary tree.
 * @returns {number[]} - An array containing the rightmost node values from top to bottom.
 */
const rightSideView = function(root) {
    if (!root) return [];

    const result = [];
    const queue = [root];

    while (queue.length > 0) {
        let levelSize = queue.length;

        for (let i = 0; i < levelSize; i++) {
            let node = queue.shift();

            // Capture the last node of each level
            if (i === levelSize - 1) {
                result.push(node.val);
            }

            // Add left and right children to queue
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
    }

    return result;
};

// Example Test Cases
if (require.main === module) {
    function TreeNode(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    // Example Tree 1: [1,2,3,null,5,null,4]
    let root1 = new TreeNode(1);
    root1.left = new TreeNode(2);
    root1.right = new TreeNode(3);
    root1.left.right = new TreeNode(5);
    root1.right.right = new TreeNode(4);

    console.log(rightSideView(root1)); 
    // Expected output: [1, 3, 4]

    // Example Tree 2: [1,2,3,4,null,null,null,5]
    let root2 = new TreeNode(1);
    root2.left = new TreeNode(2);
    root2.right = new TreeNode(3);
    root2.left.left = new TreeNode(4);
    root2.left.left.left = new TreeNode(5);

    console.log(rightSideView(root2));
    // Expected output: [1, 3, 4, 5]

    // Example Tree 3: [1,null,3]
    let root3 = new TreeNode(1);
    root3.right = new TreeNode(3);

    console.log(rightSideView(root3)); 
    // Expected output: [1, 3]

    // Example Tree 4: Empty tree
    console.log(rightSideView(null)); 
    // Expected output: []
}

/*

Complexity Analysis:
- Time Complexity: O(n) - We visit each node once using BFS.
- Space Complexity: O(n) - In the worst case, we store all nodes in the queue (e.g., a complete binary tree).

*/

export default rightSideView;
