#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   02.02kth_node.py
@Time    :   2020/02/21 03:24:09
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

"""
实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

注意：本题相对原题稍作改动

示例：

输入： 1->2->3->4->5 和 k = 2
输出： 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# here put the import lib

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        """
        应该使用双指针的
        """
        slow, fast = head,head
        while k > 0:
            fast = fast.next
            k -= 1
        
        while fast:
            fast, slow = fast.next, slow.next
        return slow
