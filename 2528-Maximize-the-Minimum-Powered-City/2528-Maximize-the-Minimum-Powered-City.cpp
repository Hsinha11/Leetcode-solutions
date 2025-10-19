#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    long long maxPower(vector<int>& stations, int r, int k) {
        int n = stations.size();
        
        // Prefix sum to compute initial power in O(1) per city
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + stations[i];
        }
        
        // Compute initial power for each city: sum stations[max(0,i-r) .. min(n-1,i+r)]
        vector<long long> power(n);
        for (int i = 0; i < n; i++) {
            int L = max(0, i - r);
            int R = min(n - 1, i + r);
            power[i] = pref[R + 1] - pref[L];
        }
        
        // Helper function: can we make every city's power >= target using at most k additions?
        auto can = [&](long long target) -> bool {
            // Difference array for range-add simulation
            vector<long long> diff(n + 1, 0);
            long long added = 0;  // current added value affecting this city
            long long used = 0;   // total stations used
            
            for (int i = 0; i < n; i++) {
                added += diff[i];  // apply any scheduled subtractions
                long long current = power[i] + added;
                
                if (current < target) {
                    long long need = target - current;
                    used += need;
                    if (used > k) {
                        return false;
                    }
                    added += need;
                    // The added `need` affects cities from i .. i + 2*r (inclusive)
                    int end = i + 2 * r + 1;  // end index is exclusive for diff array
                    if (end <= n) {
                        diff[end] -= need;
                    }
                    // If end > n, the subtraction is beyond array; we just skip (effect runs to the end)
                }
            }
            return true;
        };
        
        // Binary search for maximum feasible min-power
        long long lo = *min_element(power.begin(), power.end());
        long long hi = *max_element(power.begin(), power.end()) + k;  // hi safe upper bound
        long long ans = lo;
        
        while (lo <= hi) {
            long long mid = lo + (hi - lo) / 2;  // avoid overflow
            if (can(mid)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        
        return ans;
    }
};

// Test cases
#include <iostream>
int main() {
    Solution sol;
    
    // Example 1: stations = [1,2,4,5,0], r = 1, k = 2
    // Expected output: 5
    vector<int> stations1 = {1, 2, 4, 5, 0};
    cout << "Example 1: " << sol.maxPower(stations1, 1, 2) << endl;  // Should output 5
    
    // Example 2: stations = [4,4,4,4], r = 0, k = 3
    // Expected output: 4
    vector<int> stations2 = {4, 4, 4, 4};
    cout << "Example 2: " << sol.maxPower(stations2, 0, 3) << endl;  // Should output 4
    
    // Additional test cases
    vector<int> stations3 = {2, 1, 3, 4, 0, 1, 1};
    cout << "Test 3: " << sol.maxPower(stations3, 2, 3) << endl;
    
    return 0;
}
