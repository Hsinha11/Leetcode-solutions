// Approach: Iterate through the array while tracking seen numbers in a hash map.
// For each value i, if 2*i is already seen or (i is even and i/2 is seen),
// then there exists a valid pair (i, j) such that arr[i] == 2 * arr[j].
// This handles zeros and negatives correctly.
// Time: O(n), Space: O(n)
class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_map<int,int> d;
        for (int i : arr) {
        if (d.find(i * 2) != d.end() || (i % 2 == 0 && d.find(i / 2) != d.end())) {
            return true;
        }
        d[i] = 1;
    }
    return false;
    }
};