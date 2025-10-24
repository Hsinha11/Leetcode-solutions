# 🔄 Rotate Array Problem

## 📘 Problem Statement
Given an array `nums`, rotate the array to the **right** by `k` steps, where `k` is non-negative.

### Example
```cpp
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]

💡 Approach

We solve this problem using a temporary vector:

Calculate k = k % n to handle cases where k is larger than the array size.

If k == 0, the array remains unchanged.

Copy the last k elements of nums into a temporary vector temp.

Shift the first n-k elements of nums to the right by k positions.

Copy elements from temp to the first k positions of nums.

This approach ensures the array is rotated in O(n) time using O(k) extra space.



Code implementation
#include <vector>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n;
        if (k == 0) return;

        vector<int> temp(nums.end() - k, nums.end());
        for (int i = n - k - 1; i >= 0; i--) {
            nums[i + k] = nums[i];
        }
        for (int i = 0; i < k; i++) {
            nums[i] = temp[i];
        }
    }
};


#include <iostream>
#include <vector>
using namespace std;

void printVector(const vector<int>& v) {
    for (int num : v) cout << num << " ";
    cout << endl;
}

int main() {
    Solution sol;

    vector<int> test1 = {1,2,3,4,5,6,7};
    sol.rotate(test1, 3);
    printVector(test1); // Expected: 5 6 7 1 2 3 4

    vector<int> test2 = {-1,-100,3,99};
    sol.rotate(test2, 2);
    printVector(test2); // Expected: 3 99 -1 -100

    vector<int> test3 = {1, 2};
    sol.rotate(test3, 0);
    printVector(test3); // Expected: 1 2

    vector<int> test4 = {};
    sol.rotate(test4, 1);
    printVector(test4); // Expected: empty
}


⏱️ Time Complexity

Shifting elements takes O(n-k) time.

Copying k elements to the temporary vector takes O(k) time.

Overall: Time Complexity = O(n)

💾 Space Complexity

Temporary vector temp stores k elements.

Overall: Space Complexity = O(k)