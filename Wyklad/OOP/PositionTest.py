from Position import Position

if __name__ == '__main__':
    pos1 = Position(xPosition=1, yPosition=1)
    pos2 = Position(xPosition=0, yPosition=1)

    print(pos1)
    print(pos2)
    print(pos1.distance(pos2))
    print(Position(xPosition=0, yPosition=0)
            .distance(
                    Position(xPosition=1, yPosition=1)
                    )
        )
        