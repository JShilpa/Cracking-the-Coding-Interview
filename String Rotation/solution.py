'''
Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).
'''
import unittest


def is_substring(s1, s2):
    dict = {}
    if len(s1) != len(s2):
        return False

    for i in s1:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] = dict[i] + 1

    for i in s2:
        if i not in dict:
            return False
        else:
            dict[i] -= 1
            if dict[i] == 0:
                del dict[i]

    if bool(dict):
        return False
    else:
        return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = is_substring(s1, s2)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
