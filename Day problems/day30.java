class Solution {
    public static ArrayList<Integer> getDistinctDifference(int N, int[] A) {
        // code here
        ArrayList<Integer> res = new ArrayList<>(N);
        HashSet<Integer> left = new HashSet<>();
        HashSet<Integer> right = new HashSet<>();
        for (int i = 0; i < N; i++){
            res.add(left.size());
            left.add(A[i]);
        }
        for (int j = N - 1; j >= 0; j-- ){
            res.set(j, res.get(j) - right.size());
            right.add(A[j]);
        }
        return res;
    }
}
