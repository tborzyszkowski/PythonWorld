from Animal import Animal


class Sheep(Animal):

	def __init__(self, sheep=None, position=None):
		super(Sheep, self).__init__(sheep, position)

	def clone(self):
		return Sheep(self, None)

	def initParams(self):
		self.power = 3
		self.sign = 'S'
