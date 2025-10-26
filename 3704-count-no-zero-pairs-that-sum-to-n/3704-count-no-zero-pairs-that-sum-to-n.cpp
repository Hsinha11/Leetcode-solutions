// 3704-count-no-zero-pairs-that-sum-to-n.cpp
// Problem: Count No-Zero Pairs That Sum to N
//
// Approach (short):
//   Do a digit-DP over the decimal digits of n (process from least-significant digit to
//   most-significant). At each position keep the carry (0/1) and, for each of the two numbers
//   a and b, two small flags:
//     - seen_nonzero: whether we've placed any non-zero digit so far (in less significant positions)
//     - seen_zero_after_nonzero: whether we've placed a zero after having placed a non-zero digit
//   A number's decimal representation contains no zero iff in the LSD→MSD scan we never place
//   a zero before any non-zero, and once a zero is placed after some non-zero no later non-zero
//   digits are allowed. Enforce digit-by-digit constraints a_i, b_i ∈ [0..9], arithmetic constraint
//   (a_i + b_i + carry) % 10 == n_i, and update carry. Count only assignments where both numbers
//   have at least one non-zero digit (positive) and final carry is zero.
//
// Time Complexity:
//   O(10*10 * L) transitions where L = number of digits in n (<= 16 for n <= 1e15) — effectively
//   O(L) ≃ O(log n). Very small constant factors.
//
// Space Complexity:
//   O(L * 2 * 2 * 2 * 2 * 2) for DP memo table ~ O(L) (small).
//
// Notes:
//   - Counts ordered pairs (a, b). Uses 64-bit integers for counts (n ≤ 1e15 so result ≤ n-1).
//   - This DP meticulously enforces the "no zero digit in decimal representation" constraint.

#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

int64 n;
vector<int> digs; // digits of n, LSD first
int L;
int64 dp_memo[20][2][2][2][2][2]; // pos, carry, sA, zA, sB, zB
bool seen_memo[20][2][2][2][2][2];

int64 dfs(int pos, int carry, int sA, int zA, int sB, int zB) {
    if (pos == L) {
        // final carry must be 0, and both numbers must be positive (seen_nonzero true)
        return (carry == 0 && sA && sB) ? 1 : 0;
    }
    if (seen_memo[pos][carry][sA][zA][sB][zB]) return dp_memo[pos][carry][sA][zA][sB][zB];
    seen_memo[pos][carry][sA][zA][sB][zB] = true;
    int64 &res = dp_memo[pos][carry][sA][zA][sB][zB];
    res = 0;
    int target = digs[pos];

    // iterate possible digits for a and b at this position (0..9)
    for (int da = 0; da <= 9; ++da) {
        // digit-zero rules for a:
        // - cannot place a zero if we haven't yet seen any non-zero digit (that would mean a has a zero
        //   in a lower position before any non-zero -> invalid unless whole number is 0 which is not allowed)
        if (da == 0 && !sA) continue;
        // - cannot place a non-zero if we already placed a zero after a non-zero earlier
        if (da != 0 && zA) continue;

        int nsA = sA || (da != 0);
        int nzA = zA || (da == 0 && sA); // zero after a non-zero

        for (int db = 0; db <= 9; ++db) {
            // digit-zero rules for b:
            if (db == 0 && !sB) continue;
            if (db != 0 && zB) continue;

            int nsB = sB || (db != 0);
            int nzB = zB || (db == 0 && sB);

            int sum = da + db + carry;
            if ((sum % 10) != target) continue;
            int ncarry = sum / 10;
            res += dfs(pos + 1, ncarry, nsA, nzA, nsB, nzB);
        }
    }

    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // Read input n from stdin
    // Expect single integer n (2 <= n <= 1e15)
    if (!(cin >> n)) return 0;

    // prepare digits (LSD first)
    long long temp = n;
    digs.clear();
    while (temp > 0) {
        digs.push_back((int)(temp % 10));
        temp /= 10;
    }
    L = (int)digs.size();
    // clear memo
    memset(seen_memo, 0, sizeof(seen_memo));
    memset(dp_memo, 0, sizeof(dp_memo));

    // compute result: number of ordered pairs (a,b) of positive no-zero integers with a+b=n
    int64 ans = dfs(0, 0, 0, 0, 0, 0);
    cout << ans << "\n";
    return 0;
}
