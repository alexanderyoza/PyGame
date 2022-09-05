import pygame

class gameFrame:
    def __init__(self, width, height):
        flags = pygame.RESIZABLE
        self.surface = pygame.display.set_mode((width, height), flags)
        pygame.display.flip()

    def getSurface(self):
        return self.surface

class Outline:
    def __init__(self):
        self.topLeft = (0, 0)
        self.topRight = (1790, 0)
        self.bottomLeft = (0, 1120)
        self.bottomRight = (1790, 1120)
        self.goalLeftTop = (0, 400)
        self.goalLeftBottom = (0, 720)
        self.goalRightTop = (1790, 400)
        self.goalRightBottom = (1790, 720)
        self.width = 10

    def draw(self, surface):
        pygame.draw.line(surface, pygame.Color(255,255,255), self.topLeft, self.topRight, self.width)
        pygame.draw.line(surface, pygame.Color(255,255,255), self.topLeft, self.bottomLeft, self.width)
        pygame.draw.line(surface, pygame.Color(255,255,255), self.bottomLeft, self.bottomRight, self.width)
        pygame.draw.line(surface, pygame.Color(255,255,255), self.topRight, self.bottomRight, self.width)
        pygame.draw.line(surface, pygame.Color(0,0,0), self.goalLeftTop, self.goalLeftBottom, self.width)
        pygame.draw.line(surface, pygame.Color(0,0,0), self.goalRightTop, self.goalRightBottom, self.width)

class Score:
    def __init__(self):
        self.x = 870
        self.y = 100
        self.p1Pts = 0
        self.p2Pts = 0
    def updateScore(self, surface, winner):
        if winner == -1:
            self.p1Pts += 1
        if winner == 1:
            self.p2Pts += 1
        score = str(self.p1Pts) + "   |   " + str(self.p2Pts)
        font = pygame.font.Font('freesansbold.ttf', 20)
        score = font.render(score, True, pygame.Color(255,255,255))
        self.board = surface.blit(score, (self.x, self.y))