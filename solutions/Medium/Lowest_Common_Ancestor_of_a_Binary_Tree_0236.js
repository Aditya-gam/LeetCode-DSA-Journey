/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Function: lowestCommonAncestor
 * Description: This function finds the lowest common ancestor (LCA) of two given nodes
 * in a binary tree. The LCA is the lowest node in the tree that has both `p` and `q`
 * as descendants (including the node itself).
 *
 * @param {TreeNode} root - The root of the binary tree.
 * @param {TreeNode} p - The first target node.
 * @param {TreeNode} q - The second target node.
 * @returns {TreeNode} - The lowest common ancestor of `p` and `q`.
 */
const lowestCommonAncestor = function(root, p, q) {
    // Base case: if root is null, or root matches either p or q, return root
    if (!root || root === p || root === q) {
        return root;
    }

    // Recursively search for LCA in left and right subtrees
    let left = lowestCommonAncestor(root.left, p, q);
    let right = lowestCommonAncestor(root.right, p, q);

    // If both left and right are non-null, root is the LCA
    if (left && right) {
        return root;
    }

    // If only one side is non-null, return that side (either left or right)
    return left || right;
};

// Example Test Cases
if (require.main === module) {
    function TreeNode(val) {
        this.val = val;
        this.left = this.right = null;
    }

    // Construct Example Tree: [3,5,1,6,2,0,8,null,null,7,4]
    let root = new TreeNode(3);
    root.left = new TreeNode(5);
    root.right = new TreeNode(1);
    root.left.left = new TreeNode(6);
    root.left.right = new TreeNode(2);
    root.right.left = new TreeNode(0);
    root.right.right = new TreeNode(8);
    root.left.right.left = new TreeNode(7);
    root.left.right.right = new TreeNode(4);

    console.log(lowestCommonAncestor(root, root.left, root.right).val);
    // Expected output: 3 (LCA of 5 and 1)

    console.log(lowestCommonAncestor(root, root.left, root.left.right.right).val);
    // Expected output: 5 (LCA of 5 and 4)

    let root2 = new TreeNode(1);
    root2.left = new TreeNode(2);
    console.log(lowestCommonAncestor(root2, root2, root2.left).val);
    // Expected output: 1 (LCA of 1 and 2)
}

/*

Complexity Analysis:
- Time Complexity: O(n) - We visit each node at most once.
- Space Complexity: O(n) - In the worst case (skewed tree), recursion depth reaches O(n).

*/

export default lowestCommonAncestor;
