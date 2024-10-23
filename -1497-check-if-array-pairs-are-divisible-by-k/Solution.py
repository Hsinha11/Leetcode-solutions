class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mp = defaultdict(int)

        for val in arr:
            rem = ((val % k) + k) % k
            mp[rem] += 1

        for rem, cnt in sorted(mp.items()):
            if not rem:
                if cnt % 2:
                    return 0

            elif rem + rem == k:
                if cnt % 2:
                    return 0

            elif mp[rem] != mp[k - rem]:
                return 0

        return 1
      
