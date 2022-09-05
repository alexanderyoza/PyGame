from operator import truediv
import pygame
import math

class PlayerLeft:
    def __init__(self, x, y):
        self.playerID = 1
        self.x = x
        self.y = y
        self.radius = 50
        self.mass = 20
        self.velx = 0
        self.vely = 0
        self.absorber = 0.6
        self.maxBallVel = 1.2
    
    def move(self, dt, other):
        self.key = pygame.key.get_pressed()
        self.velx = 0
        self.vely = 0
        if self.key[pygame.K_a]:
            if self.x - self.radius > 0:
                self.velx = -0.4
        if self.key[pygame.K_d]:
            if self.x + self.radius < 1800:
                self.velx = 0.4
        if self.key[pygame.K_w]:
            if self.y - self.radius > 0:
                self.vely = -0.4
        if self.key[pygame.K_s]:
            if self.y + self.radius < 1120:
                self.vely = 0.4

        if (math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2)) <= self.radius + other.radius): #and not(self.movingAway(other)):
            self.velx = 0
            self.vely = 0
         
        self.y += self.vely * dt
        self.x += self.velx * dt

    def draw(self, surface):
        self.circle = pygame.draw.circle(surface, pygame.Color('red'), (self.x, self.y), self.radius)

    # def movingAway(self, other):
    # if (self.x - other.x < self.radius + other.radius) and self.velx > 0:

        return True

    def reset(self, x, y):
        self.x = x
        self.y = y

class PlayerRight:
    def __init__(self, x, y):
        self.playerID = 2
        self.x = x
        self.y = y
        self.radius = 50
        self.mass = 100
        self.velx = 0
        self.vely = 0
        self.absorber = 0.6
        self.maxBallVel = 1.2
    
    def move(self, dt, other):
        self.key = pygame.key.get_pressed()
        self.velx = 0
        self.vely = 0
        if self.key[pygame.K_LEFT]:
            if self.x - self.radius > 0:
                self.velx = -0.4
        if self.key[pygame.K_RIGHT]:
            if self.x + self.radius < 1800:
                self.velx = 0.4
        if self.key[pygame.K_UP]:
            if self.y - self.radius > 0:
                self.vely = -0.4
        if self.key[pygame.K_DOWN]:
            if self.y + self.radius < 1120:
                self.vely = 0.4

        if math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2)) <= self.radius + other.radius:
            self.velx = 0
            self.vely = 0

        self.y += self.vely * dt
        self.x += self.velx * dt

    def draw(self, surface):
        self.circle = pygame.draw.circle(surface, pygame.Color('blue'), (self.x, self.y), self.radius)
    
    def reset(self, x, y):
        self.x = x
        self.y = y