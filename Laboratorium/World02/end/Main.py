from World import World
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Dandelion import Dandelion
import os


if __name__ == '__main__':
	pyWorld = World(5, 5)

	newOrg = Grass(position=Position(xPosition=2, yPosition=2), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Dandelion(position=Position(xPosition=2, yPosition=4), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Sheep(position=Position(xPosition=2, yPosition=3), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	print(pyWorld)

	for _ in range(0, 30):
		input('')
		os.system('cls')
		pyWorld.makeTurn()
		print(pyWorld)
