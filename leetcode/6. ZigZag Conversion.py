#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   6. ZigZag Conversion.py
@Time    :   2020/01/15 21:55:23
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
转化成之字形的排列
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]
        if numRows <= 2:
            zags = 0
        else:
            zags = numRows - 2
        i = 0
        while i+numRows+zags < len(s):
            for l in range(numRows):
                res[l].append(s[i])
                i+= 1
            for k in range(zags):
                res[numRows - k-2].append(s[i])
                i += 1
        for l in range(numRows):
            if i < len(s):
                res[l].append(s[i])
                i += 1
        for k in range(zags):
            if i < len(s):
                res[numRows - k-2].append(s[i])
                i += 1
        ans = ""
        for i in range(len(res)):
            ans += "".join(res[i])
        return ans

print(Solution().convert("PAYPALISHIRING", 3))


""" 
另一种解法
def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        length = len(s)
        mid = 2 * numRows - 2
        ans = ''
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                j = 0
                while i + j * mid < length:
                    ans += s[i + j * mid]
                    j += 1
            else:
                j = 0
                while j * mid - i < length:
                    if j > 0:
                        ans += s[j * mid - i]
                    if j * mid + i < length:
                        ans += s[j * mid + i]
                    j += 1
        return ans
"""