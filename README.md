# LeetCode 算法练习

按题型整理 Python 解法，每个文件包含中文思路、复杂度和原题链接。
提交到力扣时使用文件中的 `Solution`；`ListNode`、`TreeNode`、`Node`
等节点类型由对应题目提供。

## 链表

建议复习顺序：206 → 92 → 24 → 25 → 445。

| 题号 | 题目 | 核心思路 |
| --- | --- | --- |
| 206 | [反转链表](linked_list/0206_reverse_linked_list.py) | 保存后继，逐个反转 next |
| 92 | [反转链表 II](linked_list/0092_reverse_linked_list_ii.py) | 反转指定区间，再连接两端 |
| 24 | [两两交换链表中的节点](linked_list/0024_swap_nodes_in_pairs.py) | 哨兵节点与三条连接的调整 |
| 25 | [K 个一组翻转链表](linked_list/0025_reverse_nodes_in_k_group.py) | 只反转长度达到 k 的完整分组 |
| 445 | [两数相加 II](linked_list/0445_add_two_numbers_ii.py) | 反转输入，逐位相加，再反转结果 |

### 这次练习的易错点

- `cur = cur.next` 移动变量；`cur.next = pre` 修改链表连接。
- 反转前先用 `nxt = cur.next` 保存后续节点，最后用 `cur = nxt` 前进。
  `cur.next = cur` 会产生自环；先写 `pre = cur` 再写 `cur = pre` 会停在原地。
- 访问 `.next` 或 `.val` 前确认节点存在。`head` 本身就是头节点，没有 `.head` 属性。
- 反转闭区间 `[left, right]` 时，需要处理 `right - left + 1` 个节点。
- `dummy` 保留入口，`tail` 随追加移动；可能改变头节点的操作要返回并接住新头节点。
- 两数相加使用 `total = x + y + carry`、`digit = total % 10`、
  `carry = total // 10`。缺少的位按 0 处理，最终进位也要生成节点。
- 445 的当前解法会反转输入链表，结果通过新建节点生成；不反转输入的进阶解法可以使用栈。
- 通过 `self.method(...)` 调用的辅助方法，要定义在同一个类中，与其他方法保持相同缩进。

## 二叉树

| 题号 | 题目 |
| --- | --- |
| 104 | [二叉树的最大深度](binary_tree/0104_maximum_depth_of_binary_tree.py) |
| 111 | [二叉树的最小深度](binary_tree/0111_minimum_depth_of_binary_tree.py) |
| 116 | [填充每个节点的下一个右侧节点指针](binary_tree/0116_populating_next_right_pointers_in_each_node.py) |
| 117 | [填充每个节点的下一个右侧节点指针 II](binary_tree/0117_populating_next_right_pointers_in_each_node_ii.py) |
| 199 | [二叉树的右视图](binary_tree/0199_binary_tree_right_side_view.py) |
| 1609 | [奇偶树](binary_tree/1609_even_odd_tree.py) |
| 2415 | [反转二叉树的奇数层](binary_tree/2415_reverse_odd_levels_of_binary_tree.py) |
| 2583 | [二叉树中的第 K 大层和](binary_tree/2583_kth_largest_sum_in_a_binary_tree.py) |

## 本地验证

使用 Python 3.10 或更新版本，在仓库根目录运行：

```bash
python -B -m unittest discover -s tests -v
```

测试文件提供本地 `ListNode`，验证本次新增的 206、92、24、445 四题。
覆盖空链表、单节点、奇偶长度、不同反转区间、连续进位及 100 位数字。
同时检查结果是否成环，以及原地操作是否保留节点身份和值。
