import unittest


def urlify(s_, length):
    num_of_spaces = s_[:length].count(' ')
    new_length = length + num_of_spaces * 2
    new_index = new_length - 1
    for i in reversed(range(length)):
        if s_[i] == ' ':
            s_ = s_[:(new_index - 2)] + '%20' + s_[(new_index + 1):]
            new_index -= 3
        else:
            s_ = s_[:new_index] + s_[i] + s_[(new_index + 1):]
            new_index -= 1
    return s_


class TestUrlify(unittest.TestCase):
    cases = [('much ado about nothing      ', 22, 'much%20ado%20about%20nothing'),
             ('Mr John Smith    ', 13, 'Mr%20John%20Smith')]

    def test_urlify(self):
        for [test_string, length, expected] in self.cases:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()