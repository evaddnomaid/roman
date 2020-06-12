import unittest
from roman import Roman

class TestRoman(unittest.TestCase):
	"""Tests for 'Roman.py'."""

	def test_adding_x_to_x(self):
		a = Roman('x')
		b = Roman('x')

		self.assertEqual("xx", a.add(b))
		self.assertEqual("xx", b.add(a))

	def test_adding_vi_to_vi(self):
		a = Roman('i')
		b = Roman('vi')
		self.assertEqual("vii", a.add(b))
		self.assertEqual("vii", b.add(a))

	def test_adding_xi_to_vi(self):
		a = Roman('xi')
		b = Roman('vi')
		self.assertEqual("xvii", a.add(b))
		self.assertEqual("xvii", b.add(a))

if __name__ == '__main__':
	unittest.main()
