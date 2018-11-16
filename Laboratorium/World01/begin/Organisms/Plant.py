from .Organism import Organism


class Plant(Organism):

	def __init__(self, plant=None, position=None, world=None):
		super(Plant, self).__init__(plant, position, world)

	def move(self):
		result = []
		newPlant = None
		newPosition = None

		if self.ifReproduce():
			newPosition = self.getFreeNeighboringPosition(self.position)
			if newPosition is not None:
				newPlant = self.clone()
				newPlant.initParam()
				newPlant.position = newPosition
				self.power = self.power/2				# spr if int
				result.append(newPlant)
		return result

	def getFreeNeighboringPosition(self, position):
		return self.world.filterFreePositions(self.world.getNeighboringPositions(position))

	def collision(self, colisionOrganism):
		return []

