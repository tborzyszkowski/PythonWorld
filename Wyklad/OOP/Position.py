from math import sqrt

class Position(object):

	def __init__(self, xPosition, yPosition):
		self.__x = xPosition
		self.__y = yPosition

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, value):
		self.__x = value

	@property
	def y(self):
		return self.__y

	@y.setter
	def y(self, value):
		self.__y = value

	def distance(self, other):
		return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

	def __eq__(self, other):
		return (self.x == other.x) and (self.y == other.y)

	def __str__(self):
		return '({0}, {1})'.format(self.x, self.y)
