class Solution {
    public int eliminateMaximum(int[] dist, int[] speed) {
        double[] arrivals = new double[dist.length];
        for (int i = 0; i < dist.length; i++) {
            arrivals[i] = (double) dist[i] / speed[i];
        }
        
        Arrays.sort(arrivals);
        int time = 0;
        int monsters = 0;
        for (double arrivalTime : arrivals) {
            if (arrivalTime > time) {
                monsters++;
                time++;
            } else {
                return monsters;
            }
        }
        return monsters;
    }
}
