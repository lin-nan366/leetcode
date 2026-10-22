# LeetCode 算法练习

按题型整理 Python 解法，每个文件包含中文思路、复杂度和原题链接。
提交到力扣时使用文件中的 `Solution`；`ListNode`、`TreeNode`、`Node`
等节点类型由对应题目提供。

每日整理：[2026-10-22 链表练习与易错点](notes/2026-10-22_linked_list.md)。

## 链表

建议复习顺序：206 → 92 → 24 → 25 → 445。
今天的复习路线：876 → 141 / 142 → 143 → 234 / 2130；
2816 复习进位与结果头节点，203 → 3217 复习删除节点与集合查询。

| 题号 | 题目 | 核心思路 |
| --- | --- | --- |
| 206 | [反转链表](linked_list/0206_reverse_linked_list.py) | 保存后继，逐个反转 next |
| 92 | [反转链表 II](linked_list/0092_reverse_linked_list_ii.py) | 反转指定区间，再连接两端 |
| 24 | [两两交换链表中的节点](linked_list/0024_swap_nodes_in_pairs.py) | 哨兵节点与三条连接的调整 |
| 25 | [K 个一组翻转链表](linked_list/0025_reverse_nodes_in_k_group.py) | 只反转长度达到 k 的完整分组 |
| 445 | [两数相加 II](linked_list/0445_add_two_numbers_ii.py) | 反转输入，逐位相加，再反转结果 |
| 876 | [链表的中间结点](linked_list/0876_middle_of_the_linked_list.py) | 快慢指针，偶数长度返回第二个中点 |
| 141 | [环形链表](linked_list/0141_linked_list_cycle.py) | 快慢指针移动后比较节点身份 |
| 142 | [环形链表 II](linked_list/0142_linked_list_cycle_ii.py) | 相遇后，从头与相遇点同步寻找入口 |
| 143 | [重排链表](linked_list/0143_reorder_list.py) | 找中点、反转后半段、交替连接 |
| 234 | [回文链表](linked_list/0234_palindrome_linked_list.py) | 比较后恢复原链表，额外空间 O(1) |
| 2130 | [链表最大孪生和](linked_list/2130_maximum_twin_sum_of_a_linked_list.py) | 前段与反转后的后段配对求和 |
| 2816 | [翻倍以链表形式表示的数字](linked_list/2816_double_a_number_represented_as_a_linked_list.py) | 从个位乘 2，处理最后的进位 |
| 203 | [移除链表元素](linked_list/0203_remove_linked_list_elements.py) | 删除后前驱不移动，避免跳过连续目标 |
| 3217 | [从链表中移除在数组中存在的节点](linked_list/3217_delete_nodes_from_linked_list_present_in_array.py) | 数组转集合，单次遍历删除 |

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

测试文件提供本地 `ListNode`，覆盖 206、92、24、445，以及 2026-10-22 新增题目。
验证空链表、奇偶长度、不同反转区间、环与入口、回文后恢复、连续删除和最后进位。
检查节点身份、值与连接，检测意外成环，并覆盖 10000 位乘 2 和 100000 节点集合查询。
