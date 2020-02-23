#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01.07rotate_matrix.py
@Time    :   2020/02/21 16:51:19
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib

"""
给定一幅由N × N矩阵表示的图像，其中每个像素的大小为4字节，编写一种方法，将图像旋转90度。

不占用额外内存空间能否做到？

 

示例 1:

给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-matrix-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i, j, n = 0, len(matrix)-1, len(matrix)-1
        while i < j:
            for tmp in range(i, j):
                matrix[i][tmp], matrix[tmp][j], matrix[j][n-tmp], matrix[n-tmp][i] =  matrix[n-tmp][i], matrix[i][tmp],matrix[tmp][j], matrix[j][n-tmp]
            i += 1
            j -= 1

print(Solution().rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))