#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   16shuzhizhengshucifang.py
@Time    :   2020/02/23 13:41:26
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib

"""
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

 

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1/x, -n
        def exps(x, n):
            if n == 1:
                return x
            elif n & 1:
                return x * exps(x, n-1)
            else:
                return exps(x*x, n//2)
        if n == 0:
            return 1
        return exps(x, n)

print(Solution().myPow(0.00001,2147483647))