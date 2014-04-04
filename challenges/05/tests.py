#!/usr/bin/env python3

import unittest

from solution import ceaser_output, ceaser_input


class TestCesar(unittest.TestCase):

    def test_ceaser_output1(self):
        @ceaser_output(13)
        def test_function():
            return "ALEA IACTA EST"
        self.assertEqual(test_function(), "NYRN VNPGN RFG")

    def test_ceaser_output2(self):
        @ceaser_output(-13)
        def test_function():
            return "ALEA IACTA EST"
        self.assertEqual(test_function(), "NYRN VNPGN RFG")

    def test_ceaser_output3(self):
        @ceaser_output(52)
        def test_function():
            return "ALEA IACTA EST"
        self.assertEqual(test_function(), "ALEA IACTA EST")

    def test_ceaser_output4(self):
        @ceaser_output(23)
        def test_function():
            return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.assertEqual(test_function(), "XYZABCDEFGHIJKLMNOPQRSTUVW")

    def test_ceaser_output5(self):
        @ceaser_output(872136871623)
        def test_function():
            return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.assertEqual(test_function(), "RSTUVWXYZABCDEFGHIJKLMNOPQ")

    def test_ceaser_input1(self):
        @ceaser_input(-13, lambda key: key > 0)
        def test_function(name, *args):
            return '{} says: {}'.format(name, ' '.join(args))
        self.assertEqual(
            test_function('Reg', 'JUNG', 'UNIR', 'GUR', 'EBZNAF',
                          'RIRE', 'QBAR', 'SBE', 'HF?', '...'),
            "Reg says: WHAT HAVE THE ROMANS EVER DONE FOR US? ...")

    def test_ceaser_input2(self):
        @ceaser_input(3, lambda key: key > 0)
        def test_function(name, *args):
            return '{} says: {}'.format(name, ' '.join(args))
        self.assertEqual(
            test_function('George', "QEB NRFZH YOLTK", "CLU GRJMP LSBO",
                          "QEB IXWV ALD"),
            "George says: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")

    def test_ceaser_input3(self):
        @ceaser_input(-13, lambda key: key > 2)
        def test_function(name, *args):
            return '{} says: {}'.format(name, ' '.join(args))
        self.assertEqual(
            test_function('Reg', 'JUNG', 'UNIR', 'GUR', 'EBZNAF',
                          'RIRE', 'QBAR', 'SBE', 'HF?', '...'),
            "Reg says: JUNG UNIR THE ROMANS EVER DONE FOR US? ...")


if __name__ == '__main__':
    unittest.main()
