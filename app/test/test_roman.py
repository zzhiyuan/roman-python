import unittest

from app.roman import Roman


class RomanTest(unittest.TestCase):
    def test_framework_works_properly(self):
        self.assertEqual(42, 6 * 7)

    def test_convert_single_digit_roman(self):
        self.assertEqual(1, Roman.convert("I"))
        self.assertEqual(5, Roman.convert("V"))
        self.assertEqual(10, Roman.convert("X"))
        self.assertEqual(50, Roman.convert("L"))
        self.assertEqual(100, Roman.convert("C"))
        self.assertEqual(500, Roman.convert("D"))
        self.assertEqual(1000, Roman.convert("M"))

    def test_add_romans(self):
        self.assertEqual(2, Roman.convert("II"))
        self.assertEqual(3, Roman.convert("III"))
        self.assertEqual(3888, Roman.convert("MMMDCCCLXXXVIII"))

    def test_subtract_romans(self):
        self.assertEqual(4, Roman.convert("IV"))
        self.assertEqual(9, Roman.convert("IX"))
        self.assertEqual(40, Roman.convert("XL"))
        self.assertEqual(90, Roman.convert("XC"))
        self.assertEqual(400, Roman.convert("CD"))
        self.assertEqual(900, Roman.convert("CM"))

    def test_add_and_subtract_romans(self):
        self.assertEqual(46, Roman.convert("XLVI"))
        self.assertEqual(98, Roman.convert("XCVIII"))
        self.assertEqual(446, Roman.convert("CDXLVI"))
        self.assertEqual(1998, Roman.convert("MCMXCVIII"))

    def test_handle_invalid_inputs(self):
        self.assertEqual(-1, Roman.convert("A"))
        self.assertEqual(-1, Roman.convert("B"))
        self.assertEqual(-1, Roman.convert("E"))
        self.assertEqual(-1, Roman.convert("F"))
        self.assertEqual(-1, Roman.convert("G"))
        self.assertEqual(-1, Roman.convert("H"))
        self.assertEqual(-1, Roman.convert(""))

    def test_answer_the_ultimate_question(self):
        self.assertEqual(42, Roman.convert("What is the answer to the ultimate question?"))