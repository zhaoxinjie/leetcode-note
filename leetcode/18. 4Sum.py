#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   18. 4Sum.py
@Time    :   2020/01/21 14:46:57
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib

class Solution:
    def fourSum(self, nums, target: int):
        ans = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i-1] == nums[i]:
                    continue
            for j in range(i+1, len(nums)-2):
                if nums[j] == nums[j-1] and j > i+1:
                    continue
                l, r = j +1, len(nums) -1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return ans