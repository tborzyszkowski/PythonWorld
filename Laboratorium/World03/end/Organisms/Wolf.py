from .Animal import Animal
from Action import Action
from ActionEnum import ActionEnum
from Organisms.Plant import Plant
import random


class Wolf(Animal):

	def __init__(self, wolf=None, position=None, world=None):
		super(Wolf, self).__init__(wolf, position, world)

	def clone(self):
		return Wolf(self, None, None)

	def initParams(self):
		self.power = 8
		self.initiative = 5
		self.liveLength = 20
		self.powerToReproduce = 16
		self.sign = 'W'

	def move(self):
		result = []
		pomPositions = self.getNeighboringPosition()
		newPosition = None

		if pomPositions:
			newPosition = random.choice(pomPositions)
			result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
			self.lastPosition = self.position
			metOrganism = self.world.getOrganismFromPosition(newPosition)
			if metOrganism is not None and not isinstance(metOrganism, Plant):
				result.extend(metOrganism.consequences(self))
		return result

	def getNeighboringPositions(self):
		return self.world.filterPositionsWithOtherSpecies(self.world.getNeighboringPositions(self.position), Wolf)
