#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   33. Search in Rotated Sorted Array.py
@Time    :   2020/02/01 18:08:12
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib

class Solution:
    def search(self, nums, target: int) -> int:
        i, j = 0, len(nums) -1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if target >= nums[0]:
                    j = mid -1
                else:
                    i = mid +1
            else:
                if target < nums[-1]:
                    i = mid +1
                else:
                    j = mid -1
        return -1
    
print(Solution().search([4,5,6,7,0,1,2], 0))

