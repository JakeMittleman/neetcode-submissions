/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {

    private int maxDiameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        this.dfs(root);
        return this.maxDiameter-1;
    }

    public int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftSubtree = this.dfs(root.left);
        int rightSubtree = this.dfs(root.right);
        int maxi = Math.max(leftSubtree, rightSubtree);
        this.maxDiameter = Math.max(maxDiameter, 1+leftSubtree+rightSubtree);
        return 1+maxi;
    }
}
