import unittest


def find_common_letters(string1, string2):
    common_letters = []
    for letter in string1:
        if letter in string2:
            common_letters.append(letter)
    common_letters = set(common_letters)
    return common_letters


result = find_common_letters('NAINA', 'REENA')
print(result)


class TestFindCommonLetters(unittest.TestCase):
    def test_find_common_letters(self):
        self.assertEqual(find_common_letters('NAINA',
                                             'REENA'), {'A', 'N'})
        self.assertEqual(find_common_letters('HELLO', 'WORLD'), {'O', 'L'})


if __name__ == '__main__':
    unittest.main()
