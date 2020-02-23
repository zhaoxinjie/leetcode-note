#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   14jianshengzi2.py
@Time    :   2020/02/23 13:35:20
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib

"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def cuttingRope(self, n: int) -> int:
        MOD = 1000000007
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = max(max(j*(i-j),j*dp[i-j]) for j in range(1,i))
        return dp[-1]%MOD

# 953271190
print(Solution().cuttingRope(120))