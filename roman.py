class Roman:
	"""Roman numeral package"""

	def __init__(self, roman_numeral):
		"""Initialize a new roman numeral"""
		self.roman_numeral = roman_numeral
	
	def roman_numeral(self):
		return self.roman_numeral

	def add(self, x):
		return self.roman_numeral + x.roman_numeral
