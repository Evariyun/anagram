import unittest

from src.anagram import Anagram


class AnagramTest(unittest.TestCase):
    def test_unjumble(self):
        self.assertEqual(["apple"], Anagram().unjumble("leppa"), "unjumbled anagram")
        self.assertEqual(["audio"], Anagram().unjumble("duaoi"), "unjumbled anagram")

    def test_unjumble_multiple(self):
        self.assertEqual(["moist", "omits"], Anagram().unjumble("stoim"), "unjumbled anagram")


    def test_make_key_from(self):
        self.assertEqual("aelpp", Anagram().make_key_from("apple"), "making_key")
        self.assertEqual("adiou", Anagram().make_key_from("audio"), "making_key")

if __name__ == '__main__':
    unittest.main()
