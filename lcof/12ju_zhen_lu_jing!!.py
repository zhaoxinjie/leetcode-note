#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   12ju_zhen_lu_jing.py
@Time    :   2020/02/21 18:42:41
@Author  :   zhao 
@Version :   1.0
@Contact :   838985328@qq.com
@Desc    :   None
'''

# here put the import lib

"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def exist(self, board, word: str) -> bool:
        """
        新建visited数组，太耗时间和空间了，而且没用回溯，只用了dfs
        """
        n, m, l = len(board), len(board[0]), len(word)
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]

        def find(i, j, index, visited):
            if index == l:
                return True
            if i < 0 or i == n or j < 0 or j == m or visited[i*m + j] == 1 or board[i][j] != word[index]:
                return False
            else:
                v = [*visited]
                v[i*m+j] =1 
                return any([find(i+dirs[k][0], j + dirs[k][1], index+1, v) for k in range(4)])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and find(i, j, 0, visited=[0 for _ in range(n*m)]):
                    return True

        return False


print(Solution().exist([["b"],["a"],["b"],["b"],["a"]],"baa"))

# solution 回溯法，牛逼， 我是新数组保存visited，而它是直接保存在旧的board数组，所以省了很多时间和空间
class Solution1:
    def exist(self, board, word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            # 下面三行比较重要
            tmp, board[i][j] = board[i][j], '/'
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False
