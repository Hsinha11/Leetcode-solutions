class Solution {
    public int[] minDifference(int[] nums, int[][] queries) {
        int n = nums.length;
        int m = queries.length;

        // prefix[i][v] = how many times number v appears in nums[0..i]
        int[][] prefix = new int[n][101]; // since nums[i] <= 100

        // Build prefix frequency
        prefix[0][nums[0]] = 1;
        for (int i = 1; i < n; i++) {
            for (int v = 1; v <= 100; v++) {
                prefix[i][v] = prefix[i - 1][v]; // carry forward previous counts
            }
            prefix[i][nums[i]]++; // increment count of current number
        }

        int[] ans = new int[m];

        // Answer each query
        for (int qi = 0; qi < m; qi++) {
            int l = queries[qi][0];
            int r = queries[qi][1];

            int prev = -1; // last distinct number seen
            int minDiff = Integer.MAX_VALUE;

            // Scan all possible numbers from 1..100
            for (int v = 1; v <= 100; v++) {
                // Count occurrences of v in nums[l..r]
                int count = prefix[r][v] - (l > 0 ? prefix[l - 1][v] : 0);

                if (count > 0) { // if v exists in subarray
                    if (prev != -1) {
                        // update minimum difference with previous distinct value
                        minDiff = Math.min(minDiff, v - prev);
                    }
                    prev = v; // update last seen distinct value
                }
            }

            // If no pair of distinct numbers, return -1
            ans[qi] = (minDiff == Integer.MAX_VALUE ? -1 : minDiff);
        }

        return ans;
    }
}
