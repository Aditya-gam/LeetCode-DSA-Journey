/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val);
 *     this.left = (left===undefined ? null : left);
 *     this.right = (right===undefined ? null : right);
 * }
 */

/**
 * Function: levelOrder
 * Description: Given the root of a binary tree, this function returns a 
 * level order traversal of its nodes' values (i.e., left to right, level by level).
 *
 * @param {TreeNode} root - The root node of the binary tree.
 * @returns {number[][]} - A list of lists where each inner list contains values at a specific level.
 */
const levelOrder = function(root) {
    if (!root) return []; // Edge case: Empty tree

    let result = [];
    let queue = [root];

    while (queue.length > 0) {
        let levelSize = queue.length; // Number of nodes at the current level
        let levelNodes = [];

        for (let i = 0; i < levelSize; i++) {
            let currentNode = queue.shift(); // Dequeue the front node
            levelNodes.push(currentNode.val); // Add node value to current level list

            // Enqueue child nodes for the next level
            if (currentNode.left) queue.push(currentNode.left);
            if (currentNode.right) queue.push(currentNode.right);
        }

        result.push(levelNodes);
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

    console.log("Test 1: Basic case with root = [3,9,20,null,null,15,7]");
    let root1 = new TreeNode(3, 
        new TreeNode(9), 
        new TreeNode(20, new TreeNode(15), new TreeNode(7))
    );
    console.log(levelOrder(root1));
    // Expected output: [[3],[9,20],[15,7]]

    console.log("Test 2: Single node tree");
    let root2 = new TreeNode(1);
    console.log(levelOrder(root2));
    // Expected output: [[1]]

    console.log("Test 3: Empty tree");
    console.log(levelOrder(null));
    // Expected output: []

    console.log("Test 4: Left-skewed tree");
    let root3 = new TreeNode(1, 
        new TreeNode(2, 
            new TreeNode(3, 
                new TreeNode(4, 
                    new TreeNode(5)
                )
            )
        )
    );
    console.log(levelOrder(root3));
    // Expected output: [[1],[2],[3],[4],[5]]

    console.log("Test 5: Right-skewed tree");
    let root4 = new TreeNode(1, null, 
        new TreeNode(2, null, 
            new TreeNode(3, null, 
                new TreeNode(4, null, 
                    new TreeNode(5)
                )
            )
        )
    );
    console.log(levelOrder(root4));
    // Expected output: [[1],[2],[3],[4],[5]]

    console.log("Test 6: Large tree with mixed structure");
    let root5 = new TreeNode(10, 
        new TreeNode(5, 
            new TreeNode(2), 
            new TreeNode(7)
        ), 
        new TreeNode(15, 
            new TreeNode(12), 
            new TreeNode(20)
        )
    );
    console.log(levelOrder(root5));
    // Expected output: [[10],[5,15],[2,7,12,20]]
}

/*
Time Complexity: O(n) - Each node is visited once.
Space Complexity: O(n) - Stores nodes in queue and result array.
*/

export default levelOrder;
