import unittest


def compress(s_):
    result = ''
    count = 1
    last_char = s_[0]
    orig_len = len(s_)
    for char in s_[1:]:
        if char == last_char:
            count += 1
        else:
            result += last_char
            result += str(count)
            if len(result) >= orig_len:
                return s_
            last_char = char
            count = 1
    result += last_char
    result += str(count)
    if len(result) >= orig_len:
        return s_
    return result


class TestCompress(unittest.TestCase):
    cases = {'aaabbcc': 'a3b2c2', 'abbaaaa': 'a1b2a4', 'abbccc': 'abbccc', 'abb': 'abb'}

    def test_compress(self):
        for arg, output in self.cases.items():
            self.assertEqual(compress(arg), output)


if __name__ == '__main__':
    unittest.main()