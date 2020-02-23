#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01.01palindrome.py
@Time    :   2020/02/21 02:50:52
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib

"""
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。

 

示例1：

输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-permutation-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        m = collections.Counter(s)
        count = 0
        for _, v in m.items():
            count += v % 2
        return count <= 1


print(Solution().canPermutePalindrome("code"))

def canPermutePalindrome(self, s: str) -> bool:
    """
    使用{*s}，和s.count()
    """
        odd = 0
        for i in {*s}:
            if s.count(i) % 2 != 0:
                odd += 1
        if odd > 1:
            return False
        return True