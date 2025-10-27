// 3709-design-exam-scores-tracker.cpp
// Approach: Since record() is always called with strictly increasing time,
// we store times and prefix sums in vectors. For totalScore queries,
// we use binary search to find the prefix sum range in O(log n) time.
// Time Complexity: O(log n) per totalScore query, O(1) per record.
// Space Complexity: O(n)

#include <bits/stdc++.h>
using namespace std;

class ExamTracker {
private:
    vector<long long> times;      // stores times of exams
    vector<long long> prefixSum;  // prefix sum of scores
public:
    ExamTracker() {}

    void record(int time, int score) {
        times.push_back(time);
        if (prefixSum.empty())
            prefixSum.push_back(score);
        else
            prefixSum.push_back(prefixSum.back() + score);
    }

    long long totalScore(int startTime, int endTime) {
        // Find first index >= startTime
        int left = lower_bound(times.begin(), times.end(), startTime) - times.begin();
        // Find last index <= endTime
        int right = upper_bound(times.begin(), times.end(), endTime) - times.begin() - 1;

        if (left > right || left >= times.size() || right < 0)
            return 0;

        long long total = prefixSum[right];
        if (left > 0) total -= prefixSum[left - 1];
        return total;
    }
};
