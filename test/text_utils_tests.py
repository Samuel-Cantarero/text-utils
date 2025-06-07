import unittest

from text_utils_program import TextUtils

class TestTextUtils(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(TextUtils.count_words("Hola Buenos días"), 3)
        self.assertEqual(TextUtils.count_words("  Disfrutando del día programando  "), 4)

    def test_count_characters(self):
        self.assertEqual(TextUtils.count_characters("abc"), 3)
        self.assertEqual(TextUtils.count_characters("a b c"), 5)

    def test_reverse_text(self):
        self.assertEqual(TextUtils.reverse_text("abc"), "cba")
        self.assertEqual(TextUtils.reverse_text("Data"), "ataD")

    def test_remove_punctuation(self):
        self.assertEqual(TextUtils.remove_punctuation("Hola, ¿qué tal?"), "Hola qué tal")
        self.assertEqual(TextUtils.remove_punctuation("123.45"), "12345")

    def test_is_palindrome_true(self):
        self.assertTrue(TextUtils.is_palindrome("Anita lava la tina"))
        self.assertTrue(TextUtils.is_palindrome("Reconocer"))

    def test_is_palindrome_false(self):
        self.assertFalse(TextUtils.is_palindrome("Hola"))
        self.assertFalse(TextUtils.is_palindrome("Viva la Ciencia"))

