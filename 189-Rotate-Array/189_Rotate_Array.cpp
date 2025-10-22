#include <iostream>
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

void printVector(const vector<int>& v) {
    for (int num : v) cout << num << " ";
    cout << endl;
}

int main() {
    Solution sol;

    vector<int> test1 = {1, 2, 3, 4, 5, 6, 7};
    sol.rotate(test1, 3);
    printVector(test1); // Expected: 5 6 7 1 2 3 4

    vector<int> test2 = {-1, -100, 3, 99};
    sol.rotate(test2, 2);
    printVector(test2); // Expected: 3 99 -1 -100

    vector<int> test3 = {1, 2};
    sol.rotate(test3, 0);
    printVector(test3); // Expected: 1 2 (no change)

    vector<int> test4 = {};
    sol.rotate(test4, 1);
    printVector(test4); // Expected: empty

    return 0;
}

