class Roman:
    """Roman numeral package"""

    ordinals = {'i': 'i', 'v': 'ii', 'x': 'iii', 'l': 'iiii'}
    values = {'i': '', 'v': 'iiiii', 'x': 'vv', 'l': 'xxxxx'}

    def __init__(self, r=None):
        """Initialize a new roman numeral"""
        if r:
            self.r = r
        else:
            self.r = ''

    def __repr__(self):
        return self.r

    def add(self, x):
        """ Add this roman numeral to another (x) """
        result = Roman(self.r)
        result.r = self.r + x.r
        result.order()
        return result.r

    def order(self):
        """
        Sorts input roman characters based on corresponding self.ordinals value
        """
        zero = len('')
        one  = len('x')
        i = len('i')
        while \
            i < len(self.r) \
            and len(self.ordinals[self.r[i - one:i]]) >= len(self.ordinals[self.r[i:i + one]]):
                i += one
        if i < len(self.r):
            self.r = self.r[zero:i - one] + self.r[i:i + one] + self.r[i - one:i] + self.r[i + one:]
            self.order()

