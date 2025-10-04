class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int maxWater = 0;

        while (left < right) {
            int width = right - left;
            int h = Math.min(height[left], height[right]);
            int currentWater = width * h;
            maxWater = Math.max(maxWater, currentWater);

            if (height[left] < height[right])
                left++;
            else
                right--;
        }
        return maxWater;
    }
}
