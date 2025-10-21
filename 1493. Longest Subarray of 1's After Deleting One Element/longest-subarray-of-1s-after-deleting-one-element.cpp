#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int left = 0;
        int zero_count = 0;
        int max_length = 0;
        
        for (int right = 0; right < nums.size(); right++) {
            // Count the number of zeros in the current window
            if (nums[right] == 0) {
                zero_count++;
            }
            
            // If there is more than one zero, shrink the window from the left
            while (zero_count > 1) {
                if (nums[left] == 0) {
                    zero_count--;
                }
                left++;
            }
            
            // Calculate the length of the current window, subtracting 1 for the deleted element
            max_length = max(max_length, right - left);
        }
        
        return max_length;
    }
};

// Test cases
#include <iostream>
int main() {
    Solution sol;
    
    // Example 1: nums = [1,1,0,1]
    // Expected output: 3
    vector<int> nums1 = {1, 1, 0, 1};
    cout << "Example 1: " << sol.longestSubarray(nums1) << endl;  // Should output 3
    
    // Example 2: nums = [0,1,1,1,0,1,1,0,1]
    // Expected output: 5
    vector<int> nums2 = {0, 1, 1, 1, 0, 1, 1, 0, 1};
    cout << "Example 2: " << sol.longestSubarray(nums2) << endl;  // Should output 5
    
    // Example 3: nums = [1,1,1]
    // Expected output: 2
    vector<int> nums3 = {1, 1, 1};
    cout << "Example 3: " << sol.longestSubarray(nums3) << endl;  // Should output 2
    
    // Additional test cases
    vector<int> nums4 = {0, 0, 0, 0};
    cout << "Test 4 (all zeros): " << sol.longestSubarray(nums4) << endl;  // Should output 0
    
    vector<int> nums5 = {1, 0, 1, 0, 1, 0, 1};
    cout << "Test 5 (alternating): " << sol.longestSubarray(nums5) << endl;  // Should output 2
    
    vector<int> nums6 = {1, 1, 0, 0, 1, 1, 1, 0, 1};
    cout << "Test 6: " << sol.longestSubarray(nums6) << endl;  // Should output 4
    
    return 0;
}
