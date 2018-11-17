from World import World
from Position import Position
from Organisms.Grass import Grass

if __name__ == "__main__":
	pyWorld = World(5, 5)

	newOrg = Grass(position=Position(xPosition=2, yPosition=2), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Grass(position=Position(xPosition=2, yPosition=4), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	print(pyWorld)
