"""链表题的本地回归测试，仅依赖 Python 标准库。"""

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


if __name__ == "__main__":
    unittest.main()
