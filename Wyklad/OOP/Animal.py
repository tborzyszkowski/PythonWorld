from Organism import Organism
import random


class Animal(Organism):

	def __init__(self, animal=None, position=None):
		super(Animal, self).__init__(animal, position)

	def move(self):
		self.position.x += random.randint(-1, 1)
		self.position.y += random.randint(-1, 1)