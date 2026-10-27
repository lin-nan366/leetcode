"""1448. 统计二叉树中好节点的数目。

DFS 向下传递当前路径的最大值，节点值大于等于该最大值时计入答案。
左右子树分别接收自己的路径最大值；相等的节点也算好节点。
时间复杂度 O(n)，递归栈空间 O(h)，h 为树高。
TreeNode 由力扣提供，包含 val、left、right。

原题链接：https://leetcode.cn/problems/count-good-nodes-in-binary-tree/
"""

from __future__ import annotations


class Solution:
    def goodNodes(self, root: TreeNode | None) -> int:
        def dfs(node, path_max):
            if node is None:
                return 0

            # 判断当前节点是不是好节点，相等也算。
            count = 1 if node.val >= path_max else 0

            # 更新路径最大值，分别传给左右孩子。
            path_max = max(path_max, node.val)

            left_count = dfs(node.left, path_max)
            right_count = dfs(node.right, path_max)

            return count + left_count + right_count

        return dfs(root, float("-inf"))
