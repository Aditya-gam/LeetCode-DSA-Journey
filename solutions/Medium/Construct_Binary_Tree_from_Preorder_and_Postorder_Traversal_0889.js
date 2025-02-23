/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * Function: constructFromPrePost
 * Description: Reconstructs a binary tree given its preorder and postorder traversals.
 * - The first element of `preorder` is always the root.
 * - The last element of `postorder` is also the root.
 * - The left child is determined by the second element in `preorder`, and its subtree extends until that node appears in `postorder`.
 *
 * @param {number[]} preorder - The preorder traversal of the binary tree.
 * @param {number[]} postorder - The postorder traversal of the binary tree.
 * @return {TreeNode} - The root of the reconstructed binary tree.
 */
const constructFromPrePost = function(preorder, postorder) {
    if (!preorder.length || !postorder.length) return null;

    let root = new TreeNode(preorder[0]);
    
    // If there's only one node, return it.
    if (preorder.length === 1) return root;

    // The left subtree root is always preorder[1]
    let leftSubtreeRoot = preorder[1];
    let leftSubtreeSize = postorder.indexOf(leftSubtreeRoot) + 1; // Find size of left subtree in postorder

    // Recursively construct left and right subtrees
    root.left = constructFromPrePost(preorder.slice(1, leftSubtreeSize + 1), postorder.slice(0, leftSubtreeSize));
    root.right = constructFromPrePost(preorder.slice(leftSubtreeSize + 1), postorder.slice(leftSubtreeSize, -1));

    return root;
};

// Example Test Cases
if (require.main === module) {
    function TreeNode(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    function treeToArray(root) {
        if (!root) return [];
        let queue = [root], result = [];
        while (queue.length > 0) {
            let node = queue.shift();
            result.push(node ? node.val : null);
            if (node) {
                queue.push(node.left);
                queue.push(node.right);
            }
        }
        // Trim nulls from the end
        while (result.length > 0 && result[result.length - 1] === null) {
            result.pop();
        }
        return result;
    }

    let preorder1 = [1,2,4,5,3,6,7], postorder1 = [4,5,2,6,7,3,1];
    let tree1 = constructFromPrePost(preorder1, postorder1);
    console.log(treeToArray(tree1));
    // Expected output: [1,2,3,4,5,6,7] (Structure may vary)

    let preorder2 = [1], postorder2 = [1];
    let tree2 = constructFromPrePost(preorder2, postorder2);
    console.log(treeToArray(tree2));
    // Expected output: [1]
}

/*

Complexity Analysis:
- Time Complexity: O(n^2) in the worst case due to slicing of arrays.
- Space Complexity: O(n) due to recursive function calls.

Optimized versions could use index-based traversal to avoid slicing and improve to O(n) time complexity.

*/

export default constructFromPrePost;
