#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   16.05factorial_zeros.py
@Time    :   2020/02/14 23:28:23
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib

class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        设计一个算法，算出 n 阶乘有多少个尾随零。

        数中包含几个因子5， 就有几个零
        """
        count = 0
        while n != 0:
            n = n // 5
            count += n
        return count