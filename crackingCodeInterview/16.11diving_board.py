#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   16.11diving_board.py
@Time    :   2020/02/15 08:18:35
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib
"""
你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

返回的长度需要从小到大排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diving-board-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if not k:
            return []
        res = [k*shorter]
        if longer == shorter:
            return res
        for i in range(k):
            res.append(res[-1] + (longer-shorter))
        return res