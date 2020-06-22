import unittest
from roman import Roman

class TestRoman(unittest.TestCase):
    """Tests for 'Roman.py'."""

    def test_adding_x_to_x(self):
        """ Test adding 10 + 10 """
        numeral_a = Roman('x')
        numeral_b = Roman('x')

        self.assertEqual('xx', numeral_a.add(numeral_b))
        self.assertEqual('xx', numeral_b.add(numeral_a))

    def test_adding_i_to_vi(self):
        """ Test adding 1 + 6 """
        numeral_a = Roman('i')
        numeral_b = Roman('vi')
        self.assertEqual('vii', numeral_a.add(numeral_b))
        self.assertEqual('vii', numeral_b.add(numeral_a))

    def test_adding_xi_to_vi(self):
        """ Test adding 11 + 6 """
        numeral_a = Roman('xi')
        numeral_b = Roman('vi')
        self.assertEqual('xvii', numeral_a.add(numeral_b))
        self.assertEqual('xvii', numeral_b.add(numeral_a))

    def test_adding_l_to_i(self):
        """ Test adding 50 + 1 """
        numeral_a = Roman('l')
        numeral_b = Roman('i')
        self.assertEqual('li', numeral_a.add(numeral_b))
        self.assertEqual('li', numeral_b.add(numeral_a))

    # def test_empty_init(self):
    #     """ Test creating an 'empty' numeral (controversial!) """
    #     numeral_a = Roman()
    #     self.assertEqual('', numeral_a)

if __name__ == '__main__':
    unittest.main()
