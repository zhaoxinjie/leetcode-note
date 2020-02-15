#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   16.07maximum.py
@Time    :   2020/02/14 23:32:18
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib

class Solution:
    def maximum(self, a: int, b: int) -> int:
        return int((a + b)/ 2 + abs((a-b)/2))