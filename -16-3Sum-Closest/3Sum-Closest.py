def threeSumClosest(nums, target):
    nums.sort()
    closest = float('inf')
    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1
        while l < r:
            tot = nums[i] + nums[l] + nums[r]
            if abs(tot - target) < abs(closest - target):
                closest = tot
            if tot < target:
                l += 1
            elif tot > target:
                r -= 1
            else:
                return tot
    return closest
