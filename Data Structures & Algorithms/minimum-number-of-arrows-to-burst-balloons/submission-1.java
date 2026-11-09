class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, (a, b) -> {
            if (a[0] <= b[0]) {
                return -1;
            }
            return 1;
        });
        int low = points[0][0];
        int high = points[0][1];

        int arrows = points.length;

        for (int i = 1; i < points.length; i++) {
            int[] point = points[i];
            if (point[0] <= high) {
                low = Math.min(low, point[0]);
                high = Math.min(high, point[1]);
                arrows -= 1;
            } else {
                low = point[0];
                high = point[1];
            }
        }
        return arrows;
    }
}
