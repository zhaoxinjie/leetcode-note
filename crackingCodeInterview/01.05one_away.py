#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01.05one_away.py
@Time    :   2020/02/20 01:57:31
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib
"""
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

 

示例 1:

输入: 
first = "pale"
second = "ple"
输出: True

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/one-away-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first) - len(second)) > 1:
            return False

        # 长度类似时
        if len(first) > len(second):
            first, second = second, first
        i,j = 0, 0
        while i < len(first) and j < len(second):
            if first[i] == second[j]:
                i += 1
                j += 1
            else:
                # 3种情况，1，first增加一个字母，2，first替换一个字母，（3.删除和增加一样）
                return first[i:] == second[j+1:] or first[i+1:] == second[j+1:]
        return True

print(Solution().oneEditAway("pale","ple"))