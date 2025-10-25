/**
 * LeetCode 278. First Bad Version
 * Approach: Binary Search to minimize API calls.
 * Time Complexity: O(log n)
 * Space Complexity: O(1)
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    return function(n) {
        let left = 1, right = n;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    };
};
