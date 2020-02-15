#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   11. Container With Most Water.py
@Time    :   2020/01/28 14:25:35
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib

class Solution:
    def maxArea(self, height) -> int:
        # ans = 0
        # for i in range(len(height) -1):
        #     for j in range(i+1, len(height)):
        #         ans = max(ans, min(height[i], height[j]) * (j - i))
        # return ans
        l, r = 0, len(height) -1
        ans = min(height[l], height[r]) * (r - l)
        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            ans = max(ans, min(height[r], height[l]) * (r - l))
        return ans

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
