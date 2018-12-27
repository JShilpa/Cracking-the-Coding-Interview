# O(N)
import unittest

def unique(string):
    # Character set is ASCII

    if len(string) > 128:
        return False

    character_set = [False for _ in range(128)]
    print(character_set)

    for i in string:
        index = ord(i)
        print(index)
        if character_set[index] != True:
            character_set[index] = True
        else:
            return False
    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()