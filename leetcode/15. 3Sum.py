#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   15. 3Sum.py
@Time    :   2020/01/21 14:16:05
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib
class Solution:
    def threeSum(self, nums):
        ans = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums) -1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    # 去重
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1; right -= 1

        return ans

print(Solution().threeSum([0,0,0]))