import unittest


def is_palindrome_permutation(s_):
    char_counts = {}
    for char in s_:
        if char != ' ':
            if 'A' <= char <= 'Z':
                char = chr(ord(char) - ord('A') + ord('a'))
            char_counts[char] = char_counts.get(char, 0) + 1
    odd_chars = [char for char, count in char_counts.items() if count % 2 == 1]
    return len(odd_chars) < 2


class TestPalindromePermutations(unittest.TestCase):
    cases = {'Tact Coa': True,
             'jhsabckuj ahjsbckj': True,
             'Able was I ere I saw Elba': True,
             'So patient a nurse to nurse a patient so': False,
             'Random Words': False,
             'Not a Palindrome': False,
             'no x in nixon': True,
             'azAZ': True}

    def test(self):
        for arg, output in self.cases.items():
            res = is_palindrome_permutation(arg)
            print(arg)
            self.assertEqual(res, output)


if __name__ == '__main__':
    unittest.main()
