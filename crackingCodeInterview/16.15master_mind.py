#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   16.15master_mind.py
@Time    :   2020/02/15 08:41:57
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib
"""
珠玑妙算游戏（the game of master mind）的玩法如下。

计算机有4个槽，每个槽放一个球，颜色可能是红色（R）、黄色（Y）、绿色（G）或蓝色（B）。例如，计算机可能有RGGB 4种（槽1为红色，槽2、3为绿色，槽4为蓝色）。作为用户，你试图猜出颜色组合。打个比方，你可能会猜YRGB。要是猜对某个槽的颜色，则算一次“猜中”；要是只猜对颜色但槽位猜错了，则算一次“伪猜中”。注意，“猜中”不能算入“伪猜中”。

给定一种颜色组合solution和一个猜测guess，编写一个方法，返回猜中和伪猜中的次数answer，其中answer[0]为猜中的次数，answer[1]为伪猜中的次数。

示例：

输入： solution="RGBY",guess="GGRR"
输出： [1,1]
解释： 猜中1次，伪猜中1次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/master-mind-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        a = 0
        b = 0
        for i in range(4):
            if solution[i] == guess[i]:
                a += 1
        s = set(solution).intersection(set(guess))
        for c in s:
            m,n = 0, 0
            for i in range(4):
                if solution[i] == c:
                    m += 1
                if guess[i] == c:
                    n += 1
            b += min(m, n)
        return [a, b-a]