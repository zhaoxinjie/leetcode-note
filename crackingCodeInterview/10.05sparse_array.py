#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   10.05sparse_array.py
@Time    :   2020/02/14 23:02:07
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib

class Solution:
    def findString(self, words, s: str):
        """
        稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。
        """
        def search(i, j):
            while i <= j:
                mid = (i+j)//2
                if words[mid] == "":
                    if search(i, mid-1) == -1:
                        return search(mid +1, j)
                    else:
                        return search(i, mid -1)
                else:
                    if words[mid] == s:
                        return mid
                    elif words[mid] < s:
                        i = mid +1
                    else:
                        j = mid -1
            return -1
        return search(0, len(words)-1)

print(Solution().findString(words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"))