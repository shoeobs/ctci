"""
Given two strings, write a method to decide if one is a permutation of the other
"""

import unittest


def are_permutations_sort(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


def are_permutations_char_counts(s1, s2):
    if len(s1) != len(s2):
        return False
    char_counts = {}
    for c1, c2 in zip(s1, s2):
        char_counts[c1] = char_counts.get(c1, 0) + 1
        char_counts[c2] = char_counts.get(c2, 0) - 1
    for char in char_counts.values():
        if char != 0:
            return False
    return True


class TestPermutations(unittest.TestCase):
    case_true = [['abc', 'cab'], ['x', 'x'], ['', '']]
    case_false = [['ab', 'a'], ['abd', 'dac'], ['', 'b']]
    def test_are_permutations_sort(self):
        for strings in self.case_true:
            self.assertTrue(are_permutations_sort(*strings))
        for strings in self.case_false:
            self.assertFalse(are_permutations_sort(*strings))
    def test_are_permutations_char_counts(self):
        for strings in self.case_true:
            self.assertTrue(are_permutations_char_counts(*strings))
        for strings in self.case_false:
            self.assertFalse(are_permutations_char_counts(*strings))


if __name__ == '__main__':
    unittest.main()