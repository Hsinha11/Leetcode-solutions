def fourSum(nums, target):
    nums.sort()
    res, n = [], len(nums)
    for i in range(n):
        for j in range(i+1, n):
            l, r = j+1, n-1
            while l < r:
                s = nums[i] + nums[j] + nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: l+=1
                    while l < r and nums[r] == nums[r+1]: r-=1
                elif s < target:
                    l += 1
                else:
                    r -= 1
    # Remove duplicates
    return list(map(list, set(map(tuple, res))))
