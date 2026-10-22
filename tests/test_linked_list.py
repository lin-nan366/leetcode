"""链表题的本地回归测试，仅依赖 Python 标准库。"""

from itertools import product
from pathlib import Path
import runpy
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def load_solution(filename):
    namespace = runpy.run_path(
        str(ROOT / "linked_list" / filename),
        init_globals={"ListNode": ListNode},
    )
    return namespace["Solution"]()


def build(values):
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def collect(head):
    """返回节点对象，检测重复访问，避免错误链表让测试无限遍历。"""
    nodes = []
    seen = set()
    while head is not None:
        if id(head) in seen:
            raise AssertionError("Result contains a cycle")
        seen.add(id(head))
        nodes.append(head)
        head = head.next
    return nodes


def cycle_cases():
    """重复节点值，枚举无环、自环、入口在头部或内部的情况。"""
    for size in range(9):
        for pos in range(-1, size):
            head = build([1] * size)
            nodes = collect(head)
            if pos >= 0:
                nodes[-1].next = nodes[pos]
            yield size, pos, head, nodes


class LinkedListTests(unittest.TestCase):
    def assert_node_order(self, head, expected_nodes, expected_values):
        actual = collect(head)
        self.assertEqual(actual, expected_nodes)
        self.assertEqual([node.val for node in actual], expected_values)

    def test_reverse_list(self):
        solution = load_solution("0206_reverse_linked_list.py")
        for values in ([], [1], [1, 2], [1, 2, 3, 4, 5], [1, 1, 2, 1]):
            with self.subTest(values=values):
                head = build(values)
                original = collect(head)
                result = solution.reverseList(head)
                self.assert_node_order(result, original[::-1], values[::-1])

    def test_reverse_between(self):
        solution = load_solution("0092_reverse_linked_list_ii.py")
        # 枚举短链表的所有合法区间，包括头部、尾部、整段和单节点。
        for size in range(1, 9):
            values = [i % 3 for i in range(size)]
            for left in range(1, size + 1):
                for right in range(left, size + 1):
                    with self.subTest(size=size, left=left, right=right):
                        head = build(values)
                        nodes = collect(head)
                        expected_nodes = (
                            nodes[:left - 1]
                            + nodes[left - 1:right][::-1]
                            + nodes[right:]
                        )
                        expected_values = (
                            values[:left - 1]
                            + values[left - 1:right][::-1]
                            + values[right:]
                        )
                        result = solution.reverseBetween(head, left, right)
                        self.assert_node_order(result, expected_nodes, expected_values)

    def test_swap_pairs(self):
        solution = load_solution("0024_swap_nodes_in_pairs.py")
        cases = (
            ([], []),
            ([1], [0]),
            ([1, 2], [1, 0]),
            ([1, 2, 3], [1, 0, 2]),
            ([1, 2, 3, 4], [1, 0, 3, 2]),
            ([1, 2, 3, 4, 5], [1, 0, 3, 2, 4]),
            ([1, 1, 2, 2], [1, 0, 3, 2]),
        )
        for values, order in cases:
            with self.subTest(values=values):
                head = build(values)
                original = collect(head)
                result = solution.swapPairs(head)
                self.assert_node_order(
                    result,
                    [original[i] for i in order],
                    [values[i] for i in order],
                )

    def test_add_two_numbers(self):
        solution = load_solution("0445_add_two_numbers_ii.py")
        cases = (
            (7243, 564), (243, 564), (0, 0), (9, 1), (99, 1),
            (1, 999), (999, 999), (100, 0), (0, 100), (5, 5),
            (10 ** 100 - 1, 1), (10 ** 100 - 1, 10 ** 100 - 1),
        )
        for first, second in cases:
            with self.subTest(first=first, second=second):
                l1 = build(map(int, str(first)))
                l2 = build(map(int, str(second)))
                inputs = collect(l1) + collect(l2)
                result = collect(solution.addTwoNumbers(l1, l2))
                self.assertEqual(
                    [node.val for node in result],
                    list(map(int, str(first + second))),
                )
                self.assertTrue(set(result).isdisjoint(inputs))

    def test_middle_node(self):
        solution = load_solution("0876_middle_of_the_linked_list.py")
        for size in range(16):
            with self.subTest(size=size):
                head = build([i % 3 for i in range(size)])
                nodes = collect(head)
                expected = nodes[size // 2] if nodes else None
                edges = [node.next for node in nodes]
                self.assertIs(solution.middleNode(head), expected)
                self.assertEqual([node.next for node in nodes], edges)

    def test_has_cycle(self):
        solution = load_solution("0141_linked_list_cycle.py")
        for size, pos, head, nodes in cycle_cases():
            with self.subTest(size=size, pos=pos):
                edges = [node.next for node in nodes]
                self.assertIs(solution.hasCycle(head), pos >= 0)
                self.assertEqual([node.next for node in nodes], edges)

    def test_detect_cycle(self):
        solution = load_solution("0142_linked_list_cycle_ii.py")
        for size, pos, head, nodes in cycle_cases():
            with self.subTest(size=size, pos=pos):
                expected = nodes[pos] if pos >= 0 else None
                edges = [node.next for node in nodes]
                self.assertIs(solution.detectCycle(head), expected)
                self.assertEqual([node.next for node in nodes], edges)

    def test_reorder_list(self):
        solution = load_solution("0143_reorder_list.py")
        for size in range(21):
            with self.subTest(size=size):
                values = [i % 3 for i in range(size)]
                head = build(values)
                nodes = collect(head)
                remaining = list(range(size))
                order = []
                while remaining:
                    order.append(remaining.pop(0))
                    if remaining:
                        order.append(remaining.pop())
                self.assertIsNone(solution.reorderList(head))
                self.assert_node_order(
                    head, [nodes[i] for i in order], [values[i] for i in order]
                )

    def test_palindrome_and_restoration(self):
        solution = load_solution("0234_palindrome_linked_list.py")
        for size in range(8):
            for digits in product((0, 1), repeat=size):
                with self.subTest(values=digits):
                    values = list(digits)
                    head = build(values)
                    nodes = collect(head)
                    edges = [node.next for node in nodes]
                    self.assertIs(solution.isPalindrome(head), values == values[::-1])
                    # True 和 False 两条路径都必须恢复全部原连接。
                    self.assert_node_order(head, nodes, values)
                    self.assertEqual([node.next for node in nodes], edges)

    def test_maximum_twin_sum(self):
        solution = load_solution("2130_maximum_twin_sum_of_a_linked_list.py")
        cases = [[5, 4, 2, 1], [4, 2, 2, 3], [1, 100000], [7, 7]]
        cases += [[(i * 7) % 13 + 1 for i in range(size)] for size in range(2, 22, 2)]
        for values in cases:
            with self.subTest(values=values):
                head = build(values)
                nodes = collect(head)
                expected = max(a + b for a, b in zip(values, reversed(values)))
                self.assertEqual(solution.pairSum(head), expected)
                self.assertEqual([node.val for node in nodes], values)
                collect(head)  # 改变连接后仍应保持无环。

    def test_double_it(self):
        solution = load_solution("2816_double_a_number_represented_as_a_linked_list.py")
        for number in (0, 1, 4, 5, 9, 10, 99, 189, 999, 1000, 909, 10 ** 100 - 1):
            with self.subTest(number=number):
                head = build(map(int, str(number)))
                inputs = collect(head)
                result = collect(solution.doubleIt(head))
                self.assertEqual(
                    [node.val for node in result], list(map(int, str(number * 2)))
                )
                self.assertTrue(set(result).isdisjoint(inputs))

    def test_double_it_long_number(self):
        solution = load_solution("2816_double_a_number_represented_as_a_linked_list.py")
        result = collect(solution.doubleIt(build([9] * 10000)))
        self.assertEqual([node.val for node in result], [1] + [9] * 9999 + [8])

    def test_remove_elements(self):
        solution = load_solution("0203_remove_linked_list_elements.py")
        for size in range(7):
            for digits in product((1, 2), repeat=size):
                for val in (0, 1, 2):
                    with self.subTest(values=digits, val=val):
                        values = list(digits)
                        head = build(values)
                        nodes = collect(head)
                        expected_nodes = [node for node in nodes if node.val != val]
                        expected_values = [value for value in values if value != val]
                        result = solution.removeElements(head, val)
                        self.assert_node_order(result, expected_nodes, expected_values)

    def test_delete_nodes_present_in_array(self):
        solution = load_solution("3217_delete_nodes_from_linked_list_present_in_array.py")
        cases = (
            ([1, 2, 3], [1, 2, 3, 4, 5]),
            ([1], [1, 2, 1, 2, 1, 2]),
            ([5], [1, 2, 3, 4]),
            ([1, 3], [1, 1, 2, 3, 3]),
            ([7], [7, 7, 7]),
            ([1, 1, 3], [1, 2, 3, 2]),
            ([1], []),
        )
        for nums, values in cases:
            with self.subTest(nums=nums, values=values):
                head = build(values)
                nodes = collect(head)
                original_nums = nums[:]
                expected_nodes = [node for node in nodes if node.val not in nums]
                expected_values = [value for value in values if value not in nums]
                result = solution.modifiedList(nums, head)
                self.assert_node_order(result, expected_nodes, expected_values)
                self.assertEqual(nums, original_nums)

    def test_delete_nodes_large_membership_lookup(self):
        # 模拟超时截图：大量相同节点值反复查询一个很长的数组。
        # 不设置依赖机器速度的耗时阈值，直接验证规模与结果。
        solution = load_solution("3217_delete_nodes_from_linked_list_present_in_array.py")
        head = build([50004] * 100000)
        nodes = collect(head)
        result = solution.modifiedList(list(range(1, 50001)), head)
        self.assert_node_order(result, nodes, [50004] * 100000)


if __name__ == "__main__":
    unittest.main()
