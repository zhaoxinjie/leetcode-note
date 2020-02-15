#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   16. 3Sum Closest.py
@Time    :   2020/01/28 15:00:02
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        ans = nums[0]+nums[1]+nums[len(nums)-1]
        nums.sort()
        for i in range(len(nums) -2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            l, r = i +1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return target
                elif s < target:
                    l += 1
                else:
                    r -= 1
                if abs(s - target) < abs(ans - target):
                    ans = s
        return ans

print(Solution().threeSumClosest([-1, 2, 1, -4], 1))