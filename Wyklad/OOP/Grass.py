from Plant import Plant


class Grass(Plant):

	def __init__(self, grass=None, position=None):
		super(Grass, self).__init__(grass, position)

	def clone(self):
		return Grass(self, None)

	def initParams(self):
		self.power = 0
		self.sign = 'G'
