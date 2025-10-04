from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        # prefix sum to compute initial power in O(1) per city
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + stations[i]

        # compute initial power for each city: sum stations[max(0,i-r) .. min(n-1,i+r)]
        power = [0] * n
        for i in range(n):
            L = max(0, i - r)
            R = min(n - 1, i + r)
            power[i] = pref[R + 1] - pref[L]

        # helper: can we make every city's power >= target using at most k additions?
        def can(target: int) -> bool:
            # diff array for range-add simulation; diff length n+1 so we can subtract at end index
            diff = [0] * (n + 1)
            added = 0   # current added value affecting this city
            used = 0    # total stations used

            for i in range(n):
                added += diff[i]  # apply any scheduled subtractions
                current = power[i] + added
                if current < target:
                    need = target - current
                    used += need
                    if used > k:
                        return False
                    added += need
                    # the added `need` affects cities from i .. i + 2*r (inclusive)
                    end = i + 2 * r + 1  # end index is exclusive for diff array
                    if end <= n:
                        diff[end] -= need
                    else:
                        # if end > n, the subtraction is beyond array; we just skip (effect runs to the end)
                        pass
            return True

        # binary search for maximum feasible min-power
        lo, hi = min(power), max(power) + k  # hi safe upper bound
        ans = lo
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans


# Example runs
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxPower([1,2,4,5,0], r=1, k=2))  # expected 5
    print(sol.maxPower([4,4,4,4], r=0, k=3))    # expected 4
