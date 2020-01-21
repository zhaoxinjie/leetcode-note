#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   56. Merge Intervals.py
@Time    :   2020/01/21 11:33:11
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

class Solution:
    def merge(self, intervals):
        intervals.sort(key= lambda e : e[0])
        ans = []
        if not intervals or len(intervals)<= 1:
            return intervals
        ans.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            elif intervals[i][0] <= ans[-1][1] and intervals[i][1] > ans[-1][1]:
                ans[-1][1] = intervals[i][1]
        return ans


print(Solution().merge([[1,3],[8,10],[2,6],[15,18]]))


"""
prefered code
def merge(self, intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,
    return out
"""