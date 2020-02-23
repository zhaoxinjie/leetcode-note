#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   14jianshengzi.py
@Time    :   2020/02/22 18:53:42
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib

class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = max(max(j*(i-j),j*dp[i-j]) for j in range(1,i))
        return dp[-1]

print(Solution().cuttingRope(4))
