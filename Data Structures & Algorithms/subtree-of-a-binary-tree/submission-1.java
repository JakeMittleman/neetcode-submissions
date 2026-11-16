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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (stack.size() > 0) {
            TreeNode node = stack.pop();
            if (node == null) {
                continue;
            }
            if (node != null && subRoot != null && node.val == subRoot.val) {
                boolean sameTree = this.sameTree(node, subRoot);
                if (sameTree) {
                    return true;
                }
            }
            stack.push(node.left);
            stack.push(node.right);
        }
        return false;
    }

    public boolean sameTree(TreeNode root, TreeNode root2) {
        Stack<TreeNode> leftTree = new Stack<>();
        Stack<TreeNode> rightTree = new Stack<>();
        leftTree.push(root);
        rightTree.push(root2);
        while (leftTree.size() > 0 && rightTree.size() > 0) {
            TreeNode leftRoot = leftTree.pop();
            TreeNode rightRoot = rightTree.pop();
            if (leftRoot == null && rightRoot == null) {
                continue;
            } else if (leftRoot == null && rightRoot != null) {
                return false;
            } else if (leftRoot != null && rightRoot == null) {
                return false;
            }
            if (leftRoot.val == rightRoot.val) {
                leftTree.push(leftRoot.left);
                leftTree.push(leftRoot.right);
                rightTree.push(rightRoot.left);
                rightTree.push(rightRoot.right);
            } else {
                return false;
            }
        }
        return true;
    }
}
