from Position import Position
from Sheep import Sheep
from Grass import Grass

if __name__ == '__main__':
    grass = Grass(position=Position(10, 10))
    sheep = Sheep(position=Position(-10, -10))

    for i in range(0,10):
        print('-- Iteration {0} --'.format(i))
        grass.move()
        print(grass)
        sheep.move()
        print(sheep)