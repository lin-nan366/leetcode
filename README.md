# LeetCode �㷨��ϰ

���������� Python �ⷨ��ÿ���ļ���������˼·�����ӶȺ�ԭ�����ӡ�
�ύ������ʱʹ���ļ��е� `Solution`��`ListNode`��`TreeNode`��`Node`
�Ƚڵ������ɶ�Ӧ��Ŀ�ṩ��

ÿ��������

- [2026-10-22 ������ϰ���״���](notes/2026-10-22_linked_list.md)
- [2026-10-23 ˫ָ����ϰ���״���](notes/2026-10-23_two_pointers.md)

## Array Algorithms

Solutions are stored in `array_algorithms` with English filenames.

| Number | Problem | Core Idea |
| --- | --- | --- |
| 88 | [Merge Sorted Array](array_algorithms/0088_merge_sorted_array.py) | Fill reserved positions from index m, then sort nums1 in place |

## Math Algorithms

Solutions are stored in `math_algorithms` with English filenames.

| Number | Problem | Core Idea |
| --- | --- | --- |
| 2535 | [Difference Between Element Sum and Digit Sum of an Array](math_algorithms/2535_difference_between_element_sum_and_digit_sum_of_an_array.py) | Array traversal and digit extraction using modulo and integer division |

## ˫ָ��

2026-10-23 ������ 6 ���⣬������� `two_pointers`��������λ�����Ӣ��������������ʽ��

| ��� | ��Ŀ | ����˼· |
| --- | --- | --- |
| 42 | [����ˮ](two_pointers/0042_trapping_rain_water.py) | �Ƚ��������߶ȣ�ÿ�ν���һ����ˮ |
| 125 | [��֤���Ĵ�](two_pointers/0125_valid_palindrome.py) | ������ĸ���֡�תСд���ٴ����˱Ƚ� |
| 2105 | [��ֲ�ｽˮ II](two_pointers/2105_watering_plants_ii.py) | ÿ�ֲ�ˮ��������ˮ���м�һ�굥���ж� |
| 16 | [��ӽ�������֮��](two_pointers/0016_3sum_closest.py) | ��С�������Ӧ�ĺ�ͬ������ |
| 15 | [����֮��](two_pointers/0015_3sum.py) | �̶�һ�������ҵ��𰸺��ƶ�ָ�벢�����ظ�ֵ |
| 611 | [��Ч�����εĸ���](two_pointers/0611_valid_triangle_number.py) | �̶���ߣ�һ���ۼ�һ�κϷ��±� |

## ����

���鸴ϰ˳��206 �� 92 �� 24 �� 25 �� 445��
����ĸ�ϰ·�ߣ�876 �� 141 / 142 �� 143 �� 234 / 2130��
2816 ��ϰ��λ����ͷ�ڵ㣬203 �� 3217 ��ϰɾ���ڵ��뼯�ϲ�ѯ��

| ��� | ��Ŀ | ����˼· |
| --- | --- | --- |
| 206 | [��ת����](linked_list/0206_reverse_linked_list.py) | �����̣������ת next |
| 92 | [��ת���� II](linked_list/0092_reverse_linked_list_ii.py) | ��תָ�����䣬���������� |
| 24 | [�������������еĽڵ�](linked_list/0024_swap_nodes_in_pairs.py) | �ڱ��ڵ����������ӵĵ��� |
| 25 | [K ��һ�鷭ת����](linked_list/0025_reverse_nodes_in_k_group.py) | ֻ��ת���ȴﵽ k ���������� |
| 445 | [������� II](linked_list/0445_add_two_numbers_ii.py) | ��ת���룬��λ��ӣ��ٷ�ת��� |
| 876 | [�������м���](linked_list/0876_middle_of_the_linked_list.py) | ����ָ�룬ż�����ȷ��صڶ����е� |
| 141 | [��������](linked_list/0141_linked_list_cycle.py) | ����ָ���ƶ���ȽϽڵ����� |
| 142 | [�������� II](linked_list/0142_linked_list_cycle_ii.py) | �����󣬴�ͷ��������ͬ��Ѱ����� |
| 143 | [��������](linked_list/0143_reorder_list.py) | ���е㡢��ת���Ρ��������� |
| 234 | [��������](linked_list/0234_palindrome_linked_list.py) | �ȽϺ�ָ�ԭ����������ռ� O(1) |
| 2130 | [�������������](linked_list/2130_maximum_twin_sum_of_a_linked_list.py) | ǰ���뷴ת��ĺ�������� |
| 2816 | [������������ʽ��ʾ������](linked_list/2816_double_a_number_represented_as_a_linked_list.py) | �Ӹ�λ�� 2���������Ľ�λ |
| 203 | [�Ƴ�����Ԫ��](linked_list/0203_remove_linked_list_elements.py) | ɾ����ǰ�����ƶ���������������Ŀ�� |
| 3217 | [���������Ƴ��������д��ڵĽڵ�](linked_list/3217_delete_nodes_from_linked_list_present_in_array.py) | ����ת���ϣ����α���ɾ�� |

### �����ϰ���״���

- `cur = cur.next` �ƶ�������`cur.next = pre` �޸��������ӡ�
- ��תǰ���� `nxt = cur.next` ��������ڵ㣬����� `cur = nxt` ǰ����
  `cur.next = cur` ������Ի�����д `pre = cur` ��д `cur = pre` ��ͣ��ԭ�ء�
- ���� `.next` �� `.val` ǰȷ�Ͻڵ���ڡ�`head` ��������ͷ�ڵ㣬û�� `.head` ���ԡ�
- ��ת������ `[left, right]` ʱ����Ҫ���� `right - left + 1` ���ڵ㡣
- `dummy` ������ڣ�`tail` ��׷���ƶ������ܸı�ͷ�ڵ�Ĳ���Ҫ���ز���ס��ͷ�ڵ㡣
- �������ʹ�� `total = x + y + carry`��`digit = total % 10`��
  `carry = total // 10`��ȱ�ٵ�λ�� 0 ���������ս�λҲҪ���ɽڵ㡣
- 445 �ĵ�ǰ�ⷨ�ᷴת�������������ͨ���½��ڵ����ɣ�����ת����Ľ��׽ⷨ����ʹ��ջ��
- ͨ�� `self.method(...)` ���õĸ���������Ҫ������ͬһ�����У�����������������ͬ������

## ������

| ��� | ��Ŀ |
| --- | --- |
| 104 | [��������������](binary_tree/0104_maximum_depth_of_binary_tree.py) |
| 111 | [����������С���](binary_tree/0111_minimum_depth_of_binary_tree.py) |
| 116 | [���ÿ���ڵ����һ���Ҳ�ڵ�ָ��](binary_tree/0116_populating_next_right_pointers_in_each_node.py) |
| 117 | [���ÿ���ڵ����һ���Ҳ�ڵ�ָ�� II](binary_tree/0117_populating_next_right_pointers_in_each_node_ii.py) |
| 199 | [������������ͼ](binary_tree/0199_binary_tree_right_side_view.py) |
| 1448 | [ͳ�ƶ������кýڵ����Ŀ](binary_tree/1448_count_good_nodes_in_binary_tree.py) |
| 1609 | [��ż��](binary_tree/1609_even_odd_tree.py) |
| 2415 | [��ת��������������](binary_tree/2415_reverse_odd_levels_of_binary_tree.py) |
| 2583 | [�������еĵ� K ����](binary_tree/2583_kth_largest_sum_in_a_binary_tree.py) |

## ������֤

ʹ�� Python 3.10 ����°汾���ڲֿ��Ŀ¼���У�

```bash
python -B -m unittest discover -s tests -v
```

�����ļ��ṩ���� `ListNode`������ 206��92��24��445���Լ� 2026-10-22 ������Ŀ��
��֤����������ż���ȡ���ͬ��ת���䡢������ڡ����ĺ�ָ�������ɾ��������λ��
���ڵ����ݡ�ֵ�����ӣ��������ɻ��������� 10000 λ�� 2 �� 100000 �ڵ㼯�ϲ�ѯ��

`tests/test_two_pointers.py` ���� 2026-10-23 �� 6 ���⣬�������������������
ʹ�����м��㡢��Ԫ����ٺͶ����Ľ�ˮģ��˶Խ��������ظ���ϡ��ϸ������β���ʽ��
���˺���ַ�������ż�������м䲹ˮ�������Ǵ����ظ�ֵ�ļ�����ȥ�ء�
