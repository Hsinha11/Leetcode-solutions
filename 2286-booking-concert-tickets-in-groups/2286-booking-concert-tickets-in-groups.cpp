// 2286-booking-concert-tickets-in-groups.cpp
// Approach: Keep start[row] = next free seat index for each row (free seats are a suffix).
// Build a segment tree storing for each node: sumFree (total free seats) and maxFree (max free seats in any row).
// gather: find leftmost row <= maxRow with maxFree >= k, allocate k at start[row], update tree.
// scatter: if sumFree over [0..maxRow] >= k, greedily allocate from low rows.
// Time: gather O(log n), scatter O(r log n) where r rows are touched (amortized good).
// Space: O(n)

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct BookMyShow {
    int n;
    ll m;
    vector<ll> start;      // next free seat per row
    int size;
    vector<ll> sumTree;    // total free seats
    vector<ll> maxTree;    // max free seats in any row

    BookMyShow(int n_, ll m_) : n(n_), m(m_) {
        n = n_;
        m = m_;
        start.assign(n, 0);
        size = 1;
        while (size < n) size <<= 1;
        sumTree.assign(2*size, 0);
        maxTree.assign(2*size, 0);
        for (int i = 0; i < n; ++i) {
            sumTree[size + i] = m;
            maxTree[size + i] = m;
        }
        for (int i = size - 1; i >= 1; --i) {
            sumTree[i] = sumTree[2*i] + sumTree[2*i + 1];
            maxTree[i] = max(maxTree[2*i], maxTree[2*i + 1]);
        }
    }

    void update_row(int idx) {
        int node = size + idx;
        ll val = m - start[idx];
        sumTree[node] = val;
        maxTree[node] = val;
        node >>= 1;
        while (node >= 1) {
            sumTree[node] = sumTree[2*node] + sumTree[2*node + 1];
            maxTree[node] = max(maxTree[2*node], maxTree[2*node + 1]);
            node >>= 1;
        }
    }

    ll query_sum(int l, int r) {
        l += size; r += size;
        ll res = 0;
        while (l <= r) {
            if (l & 1) res += sumTree[l++];
            if (!(r & 1)) res += sumTree[r--];
            l >>= 1; r >>= 1;
        }
        return res;
    }

    ll query_max(int l, int r) {
        l += size; r += size;
        ll res = 0;
        while (l <= r) {
            if (l & 1) res = max(res, maxTree[l++]);
            if (!(r & 1)) res = max(res, maxTree[r--]);
            l >>= 1; r >>= 1;
        }
        return res;
    }

    // find leftmost row in [ql, qr] with maxFree >= k, or -1
    int find_row_with_at_least(int ql, int qr, ll k) {
        function<int(int,int,int)> descend = [&](int node, int nl, int nr) -> int {
            if (nl > qr || nr < ql || maxTree[node] < k) return -1;
            if (nl == nr) return nl;
            int mid = (nl + nr) >> 1;
            int left = descend(node*2, nl, mid);
            if (left != -1) return left;
            return descend(node*2 + 1, mid + 1, nr);
        };
        return descend(1, 0, size - 1);
    }

    // gather
    vector<int> gather(int k, int maxRow) {
        if (maxRow < 0) return {};
        maxRow = min(maxRow, n - 1);
        if (query_max(0, maxRow) < k) return {};
        int row = find_row_with_at_least(0, maxRow, k);
        if (row == -1 || row >= n) return {};
        int seat = (int)start[row];
        start[row] += k;
        update_row(row);
        return {row, seat};
    }

    // scatter
    bool scatter(int k, int maxRow) {
        if (maxRow < 0) return false;
        maxRow = min(maxRow, n - 1);
        ll total = query_sum(0, maxRow);
        if (total < k) return false;
        int row = 0;
        while (k > 0 && row <= maxRow) {
            ll free = m - start[row];
            if (free > 0) {
                ll take = min<ll>(free, k);
                start[row] += take;
                update_row(row);
                k -= (int)take;
            }
            ++row;
        }
        return true;
    }
};

// Example main (local testing)
int main() {
    BookMyShow b(2, 5);
    auto a = b.gather(4, 0); // [0,0]
    if (a.empty()) cout << "[]\n"; else cout << "[" << a[0] << "," << a[1] << "]\n";
    auto b2 = b.gather(2, 0); // []
    if (b2.empty()) cout << "[]\n"; else cout << "[" << b2[0] << "," << b2[1] << "]\n";
    cout << (b.scatter(5,1) ? "true\n" : "false\n"); // true
    cout << (b.scatter(5,1) ? "true\n" : "false\n"); // false
    return 0;
}
