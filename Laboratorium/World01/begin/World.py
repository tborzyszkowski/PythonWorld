from .Position import Position
from .Organisms.Plant import Plant


class World(object):

	def __init__(self, worldX, worldY):
		self.__worldX = worldX
		self.__worldY = worldY
		self.__turn = 0
		self.__organisms = []
		self.__newOrganisms = []
		self.__separator = ' '

	@property
	def wordlX(self):
		return self.__worldX

	@property
	def worldY(self):
		return self.__worldY

	@property
	def turn(self):
		return self.__turn

	@property
	def organisms(self):
		return self.__organisms

	@property
	def newOrganisms(self):
		return self.__newOrganisms

	@property
	def separator(self):
		return self.__separator

	def makeTurn(self):
		pass

	def addOrganism(self):
		pass

	def positionOnBoard(self, position):
		return position.x >= 0 and position.y >= 0 and position.x < self.wordlX and position.y < self.worldY

	def getOrganismFromPosition(self, position):
		pomOrganism = None

		for org in self.organisms:
			if org.position == position:
				pomOrganism = org
				break
		if pomOrganism is None:
			for org in self.newOrganisms:
				if org.position == position:
					pomOrganism = org
					break
		return pomOrganism

	def getNeighboringPositions(self, position):
		result = []
		pomPosition = None

		for y in range(-1, 2):
			for x in range(-1, 2):
				pomPosition = Position(xPosition=position.x + x, yPosition=position.y + y)
				if self.positionOnBoard(pomPosition) and not (y == 0 and x == 0):
					result.append(pomPosition)
		return result

	def filterFreePositions(self, fields):
		result = []

		for field in fields:
			if self.getOrganismFromPosition(field) is None:
				result.append(field)
		return result

	def filterPositionsWithoutAnimals(self, fields):
		result = []
		pomOrg = None

		for filed in fields:
			pomOrg = self.getOrganismFromPosition(fields)
			if pomOrg is None or isinstance(pomOrg, Plant):
				result.append(filed)
		return result

	def __str__(self):
		result = ""
		for wY in range(0, self.wordlY):
			for wX in range(0, self.worldX):
				org = self.getOrganismFromPosition(Position(xPosition=wX, yPosition=wY))
				if org:
					result += str(org.sign)
				else:
					result += self.separator
			result += '\n'
		return result
