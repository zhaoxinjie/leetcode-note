#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   07chong_jian_er_cha_shu.py
@Time    :   2020/02/21 18:20:01
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib

"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        p1, p2, i1, i2 = 0, len(preorder)-1, 0, len(inorder)-1
        def construct(p1, p2, i1,i2):
            tmp = i1
            while tmp <= i2:
                if preorder[p1] == inorder[tmp]:
                    root = TreeNode(inorder[tmp])
                    root.left = construct(p1+1, p1+1+tmp-i1, i1, tmp-1)
                    root.right = construct(p1+1+tmp-i1, p2, tmp+1, i2)
                    return root
                else:
                    tmp += 1
            else:
                return None

        return construct(p1,p2,i1,i2)