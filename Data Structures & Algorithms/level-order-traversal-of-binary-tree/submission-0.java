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
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) {
            return new ArrayList<List<Integer>>();
        }
        List<List<Integer>> ans = new ArrayList<>();
        Queue<TreeNode> queue = new ArrayDeque<>();
        Queue<Integer> heightQueue = new ArrayDeque<>();

        queue.add(root);
        heightQueue.add(1);

        List<Integer> level = new ArrayList<>();
        int currHeight = 1;

        while (queue.size() > 0) {
            TreeNode node = queue.poll();
            Integer height = heightQueue.poll();

            if (height != currHeight) {
                if (level.size() > 0) {
                    ans.add(level);
                }
                level = new ArrayList<>();
                level.add(node.val);
                currHeight = height;
            } else {
                level.add(node.val);            
            }
            if (node.left != null) {
                queue.add(node.left);
                heightQueue.add(height+1);
            }
            if (node.right != null) {
                queue.add(node.right);
                heightQueue.add(height+1);
            }     
        }
        if (level.size() > 0) {
            ans.add(level);
        }
        return ans;
    }
}
