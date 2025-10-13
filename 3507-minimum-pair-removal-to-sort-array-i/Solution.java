class Solution {
    public int minimumPairRemoval(int[] nums) {
        int operations = 0;
        
        while (!isNonDecreasing(nums)) {
            nums = mergeMinSumPair(nums);
            operations++;
        }
        return operations;
    }

    // Check if array is non-decreasing
    private boolean isNonDecreasing(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < nums[i - 1]) return false;
        }
        return true;
    }

    // Merge the leftmost adjacent pair with the minimum sum
    private int[] mergeMinSumPair(int[] nums) {
        int n = nums.length;
        int minSum = Integer.MAX_VALUE;
        int index = -1;

        // Find leftmost min sum pair
        for (int i = 0; i < n - 1; i++) {
            int sum = nums[i] + nums[i + 1];
            if (sum < minSum) {
                minSum = sum;
                index = i;
            }
        }

        // Create new array after merging
        int[] newNums = new int[n - 1];
        int j = 0;
        for (int i = 0; i < n; i++) {
            if (i == index) {
                newNums[j++] = nums[i] + nums[i + 1];
                i++; // skip next element (since merged)
            } else {
                newNums[j++] = nums[i];
            }
        }
        return newNums;
    }
}