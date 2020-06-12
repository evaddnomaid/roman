class Roman:
	"""Roman numeral package"""

	ordinals = {'i': 'i', 'v': 'ii', 'x': 'iii'}
	values   = {'i': '', 'v': 'iiiii', 'x': 'vv'}

	def __init__(self, r):
		"""Initialize a new roman numeral"""
		self.r = r
	
	def roman_numeral(self):
		return self.r

	def add(self, x):
		result = Roman(self.r)
		result.r = self.r + x.r
		result.order()
		return result.r

	def order(self):
		i = len('i')
		while i < len(self.r) and len(self.ordinals[self.r[i - 1:i]]) >= len(self.ordinals[self.r[i:i +1]]):
			i += len('i')
		if i < len(self.r):
			self.r = self.r[0:i-1] + self.r[i:i+1] + self.r[i-1:i] + self.r[i+1:]
			self.order()

