import unittest


def is_unique_chars_set(s_):
    return len(set(s_)) == len(s_)


def is_unique_chars_hash(s_):
    if len(s_) > 128:
        return False
    chars_seen = []
    for char in s_:
        if char in chars_seen:
            return False
        else:
            chars_seen.append(char)
    return True


class TestUnique(unittest.TestCase):
    case_true = ['abcd', 's4fad', '']
    case_false = ['23ds2', 'hb 627jh=j ()']

    def test_is_unique_chars_set(self):
        for case in self.case_true:
            self.assertTrue(is_unique_chars_set(case))
        for case in self.case_false:
            self.assertFalse(is_unique_chars_set(case))

    def test_is_unique_chars_hash(self):
        for case in self.case_true:
            self.assertTrue(is_unique_chars_hash(case))
        for case in self.case_false:
            self.assertFalse(is_unique_chars_hash(case))


if __name__ == '__main__':
    unittest.main()

