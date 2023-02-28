import random


class Player:

    def __init__(self, xCord, yCord):
        self.xCord = xCord
        self.yCord = yCord
        self.moveCount = 0

    def move(self, mapX, mapY):
        randomMove = random.randint(0, 3)

        # 0 -> Move Up (yCord + 1)
        # 1 -> Move Right (xCord + 1)
        # 2 -> Move Down (yCord - 1)
        # 3 -> Move Left (xCord - 1)

        match randomMove:
            case 0:
                moveUp(self, mapX, mapY)
            case 1:
                moveRight(self, mapX, mapY)
            case 2:
                moveDown(self, mapX, mapY)
            case 3:
                moveLeft(self, mapX, mapY)

        # move up if able to move up, else move right

        def moveUp(self, mapX, mapY):
            if (self.yCord+1 <= mapY):
                self.yCord += 1
                self.moveCount += 1
            else:
                moveRight(self, mapX, mapY)

        # move right if able to move right, else move down
        def moveRight(self, mapX, mapY):
            if (self.xCord+1 <= mapX):
                self.xCord += 1
                self.moveCount += 1
            else:
                moveDown(self, mapX, mapY)

        # move down if able to move down, else move left
        def moveDown(self, mapX, mapY):
            if (self.yCord-1 >= 0):
                self.yCord -= 1
                self.moveCount += 1
            else:
                moveLeft(self, mapX, mapY)

        # move left if able to move left, else move up
        def moveLeft(self, mapX, mapY):
            if (self.xCord-1 >= 0):
                self.xCord -= 1
                self.moveCount += 1
            else:
                moveUp(self, mapX, mapY)
