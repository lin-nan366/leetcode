"""双指针题的本地回归测试，用直接计算与穷举核对优化算法。"""

from itertools import combinations, combinations_with_replacement, product
from math import comb
from pathlib import Path
from random import Random
import re
import runpy
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_solution(filename):
    namespace = runpy.run_path(str(ROOT / "two_pointers" / filename))
    return namespace["Solution"]()


class TwoPointersTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rain = load_solution("0042_trapping_rain_water.py")
        cls.palindrome = load_solution("0125_valid_palindrome.py")
        cls.watering = load_solution("2105_watering_plants_ii.py")
        cls.closest = load_solution("0016_3sum_closest.py")
        cls.three_sum = load_solution("0015_3sum.py")
        cls.triangles = load_solution("0611_valid_triangle_number.py")

    def test_rain_examples_and_boundaries(self):
        cases = (
            ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
            ([4, 2, 0, 3, 2, 5], 9),
            ([2, 0, 3, 1, 2], 3),
            ([0], 0), ([2, 2], 0), ([1, 2, 3], 0),
            ([3, 2, 1], 0), ([3, 0, 0, 3], 6),
        )
        for values, expected in cases:
            with self.subTest(values=values):
                original = values[:]
                self.assertEqual(self.rain.trap(values), expected)
                self.assertEqual(values, original)

    def test_rain_against_per_column_calculation(self):
        for size in range(1, 7):
            for values in product(range(3), repeat=size):
                expected = sum(
                    min(max(values[:i + 1]), max(values[i:])) - values[i]
                    for i in range(size)
                )
                self.assertEqual(self.rain.trap(list(values)), expected, values)

    def test_palindrome_examples_and_filtering(self):
        cases = (
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False), (" ", True), (".,:!?", True),
            ("0P", False), ("a", True), ("1aA1", True),
        )
        for value, expected in cases:
            with self.subTest(value=value):
                self.assertIs(self.palindrome.isPalindrome(value), expected)

    def test_palindrome_against_ascii_filter(self):
        for size in range(5):
            for chars in product("aB0 ,", repeat=size):
                value = "".join(chars)
                cleaned = re.sub(r"[^a-z0-9]", "", value.lower())
                self.assertEqual(
                    self.palindrome.isPalindrome(value),
                    cleaned == cleaned[::-1],
                    value,
                )

    def test_watering_examples_and_delayed_refill_regression(self):
        cases = (
            ([2, 2, 3, 3], 5, 5, 1),
            ([2, 2, 3, 3], 3, 4, 2),
            ([5], 10, 8, 0),
            ([3, 2, 2, 1, 3], 4, 4, 1),
            ([3, 3, 3], 3, 3, 1),
            ([1, 2, 3, 2, 1], 3, 6, 0),
        )
        for plants, cap_a, cap_b, expected in cases:
            with self.subTest(plants=plants, capacities=(cap_a, cap_b)):
                original = plants[:]
                self.assertEqual(
                    self.watering.minimumRefill(plants, cap_a, cap_b), expected
                )
                self.assertEqual(plants, original)

    def test_watering_against_separate_paths(self):
        def water_path(needs, capacity):
            remaining = capacity
            count = 0
            for need in needs:
                if need > remaining:
                    count += 1
                    remaining = capacity
                remaining -= need
            return count, remaining

        rng = Random(2105)
        for size in range(1, 12):
            for _ in range(40):
                plants = [rng.randint(1, 5) for _ in range(size)]
                cap_a = rng.randint(max(plants), 10)
                cap_b = rng.randint(max(plants), 10)
                half = size // 2
                count_a, left = water_path(plants[:half], cap_a)
                count_b, right = water_path(reversed(plants[size - half:]), cap_b)
                expected = count_a + count_b
                if size % 2 and max(left, right) < plants[half]:
                    expected += 1
                self.assertEqual(
                    self.watering.minimumRefill(plants, cap_a, cap_b),
                    expected,
                    (plants, cap_a, cap_b),
                )

    def test_closest_examples_and_sum_not_distance(self):
        cases = (
            ([-1, 2, 1, -4], 1, 2), ([0, 0, 0], 1, 0),
            ([1, 2, 3], 6, 6), ([1, 2, 3, 4], 100, 9),
            ([-4, -2, -1, 3], -100, -7),
        )
        for values, target, expected in cases:
            with self.subTest(values=values, target=target):
                self.assertEqual(self.closest.threeSumClosest(values[:], target), expected)

    def test_closest_against_triplet_enumeration(self):
        for size in range(3, 7):
            for values in combinations_with_replacement(range(-2, 3), size):
                sums = {sum(triple) for triple in combinations(values, 3)}
                for target in (-6, -1, 0, 1, 6):
                    result = self.closest.threeSumClosest(list(reversed(values)), target)
                    self.assertIn(result, sums)
                    # 多个和同样接近时，任意一个最小距离对应的和都可接受。
                    self.assertEqual(
                        abs(result - target),
                        min(abs(total - target) for total in sums),
                        (values, target),
                    )

    def test_three_sum_examples_and_duplicates(self):
        cases = (
            ([-1, 0, 1, 2, -1, -4], [(-1, -1, 2), (-1, 0, 1)]),
            ([0, 1, 1], []), ([0, 0, 0], [(0, 0, 0)]),
            ([-2, 0, 0, 2, 2], [(-2, 0, 2)]),
            ([0] * 3000, [(0, 0, 0)]),
        )
        for values, expected in cases:
            result = self.three_sum.threeSum(values[:])
            self.assertEqual(sorted(map(tuple, result)), expected)

    def test_three_sum_against_triplet_enumeration(self):
        for size in range(3, 7):
            for values in combinations_with_replacement(range(-2, 3), size):
                expected = {
                    triple for triple in combinations(values, 3) if sum(triple) == 0
                }
                result = self.three_sum.threeSum(list(reversed(values)))
                actual = {tuple(sorted(triple)) for triple in result}
                self.assertEqual(actual, expected, values)
                self.assertEqual(len(result), len(actual), values)

    def test_triangles_examples_and_index_counting(self):
        cases = (
            ([2, 2, 3, 4], 3), ([4, 2, 3, 4], 4),
            ([2, 2, 4], 0), ([0, 0, 0], 0),
            ([0, 2, 2, 3], 1), ([1], 0), ([1, 1], 0),
            ([2] * 1000, comb(1000, 3)),
        )
        for values, expected in cases:
            self.assertEqual(self.triangles.triangleNumber(values[:]), expected)

    def test_triangles_against_triplet_enumeration(self):
        for size in range(1, 7):
            for values in combinations_with_replacement(range(4), size):
                # combinations 保留不同下标，相同边长仍应分别计数。
                expected = sum(
                    sum(triple) > 2 * max(triple)
                    for triple in combinations(values, 3)
                )
                self.assertEqual(
                    self.triangles.triangleNumber(list(reversed(values))),
                    expected,
                    values,
                )


if __name__ == "__main__":
    unittest.main()
