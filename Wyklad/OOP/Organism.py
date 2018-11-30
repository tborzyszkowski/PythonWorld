from abc import ABC, abstractmethod
from Position import Position


class Organism(ABC):

	def __init__(self, organism, position):
		self.__power = None
		self.__position = None
		self.__sign = None

		if organism is not None:
			self.__power = organism.power
			self.__position = organism.position
			self.__sign = organism.sign
		else:
			if position is not None:
				self.__position = position
			self.initParams()

	@property
	def power(self):
		return self.__power

	@power.setter
	def power(self, value):
		self.__power = value

	@property
	def position(self):
		return self.__position

	@position.setter
	def position(self, value):
		self.__position = value

	@abstractmethod
	def move(self):
		pass

	@abstractmethod
	def initParams(self):
		pass

	@abstractmethod
	def clone(self):
		pass

	def __str__(self):
		return '{0}: power: {1} position: {2}'\
				.format(self.__class__.__name__, self.power, self.position)
