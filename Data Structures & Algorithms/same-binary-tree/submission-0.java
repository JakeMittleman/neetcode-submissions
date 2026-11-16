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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        Stack<TreeNode> left = new Stack<>();
        Stack<TreeNode> right = new Stack<>();
        left.push(p);
        right.push(q);

        while (left.size() > 0 && right.size() > 0) {
            TreeNode leftNode = left.pop();
            TreeNode rightNode = right.pop();
            if (leftNode == null && rightNode == null) {
                continue;
            }
            if ((leftNode != null && rightNode == null) || (leftNode == null && rightNode != null)) {
                return false;
            }
            if (leftNode != null && rightNode != null && leftNode.val != rightNode.val) {
                return false;
            }
            left.push(leftNode.left);
            left.push(leftNode.right);
            right.push(rightNode.left);
            right.push(rightNode.right);
        }
        return true;
    }
}
