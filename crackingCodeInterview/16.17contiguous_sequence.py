#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   16.17contiguous_sequence.py
@Time    :   2020/02/15 10:04:32
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib
"""
给定一个整数数组（有正数有负数），找出总和最大的连续数列，并返回总和。

示例：

输入： [-2,1,-3,4,-1,2,1,-5,4]
输出： 6
解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶：

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contiguous-sequence-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -0x7fffffff
        pre = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > pre + nums[i]:
                pre = nums[i]
            else:
                pre += nums[i]
            ans = max(ans, pre)
        return ans
