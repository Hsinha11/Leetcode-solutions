def subarraySum(nums, k):
    from collections import defaultdict
    count = {0: 1}
    res = s = 0
    for n in nums:
        s += n
        res += count.get(s - k, 0)
        count[s] = count.get(s, 0) + 1
    return res
