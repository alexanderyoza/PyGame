import pygame
import math
import random

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mass = 10
        self.radius = 30
        self.velocity = [0, 0]
        self.outsideHBounds = False
        self.outsideVBounds = False
        self.p1NotTouching = True
        self.p2NotTouching = True
        self.winner = 0
        self.red = 255
        self.green = 255
        self.blue = 255
    
    def move(self, p1, p2, dt):
        if (self.x > 1775 or self.x < 15) and not(self.outsideVBounds):
            self.red = random.randint(0,255)
            self.green = random.randint(0,255)
            self.blue = random.randint(0,255)
            self.velocity[0] = self.velocity[0] * -1
            if self.x > 1775 and (self.y - (self.radius/2)) > 400 and (self.y + (self.radius/2)) < 720:
                self.winner = -1
            elif self.x < 15 and (self.y - (self.radius/2)) > 400 and (self.y + (self.radius/2)) < 720:
                self.winner = 1
            self.outsideVBounds = True
        else:
            self.winner = 0
            if (self.x < 1775 or self.x > 15):
                self.outsideVBounds = False
        if (self.y > 1105 or self.y < 15)  and not(self.outsideHBounds):
            self.red = random.randint(0,255)
            self.green = random.randint(0,255)
            self.blue = random.randint(0,255)
            self.velocity[1] = self.velocity[1] * -1
            self.outsideHBounds = True
        else:
            if (self.y < 1105 or self.y > 15):
                self.outsideHBounds = False
        

        if self.getDistance(p1.x, p1.y) <= (p1.radius + self.radius) and self.p1NotTouching:
            self.velocity = self.getResultantVelocity(p1)
            self.p1NotTouching = False
        else:
            self.p1NotTouching = self.collided(p1)
        if self.getDistance(p2.x, p2.y) <= (p2.radius + self.radius) and self.p2NotTouching:
            self.velocity = self.getResultantVelocity(p2)
            self.p2NotTouching = False
        else:
            self.p2NotTouching = self.collided(p2)
        if self.velocity[0] > 0:
            self.velocity[0] -= dt * 0.00005
        elif self.velocity[0] < 0:
            self.velocity[0] += dt * 0.00005
        if self.velocity[1] > 0:
            self.velocity[1] -= dt * 0.00005
        elif self.velocity[1] < 0:
            self.velocity[1] += dt * 0.00005
        

        self.x = self.x + self.velocity[0] * dt
        self.y = self.y + self.velocity[1] * dt

    def draw(self, surface):
        self.circle = pygame.draw.circle(surface, pygame.Color(self.red,self.green,self.blue), (self.x, self.y), self.radius)
    
    def collided(self, player):
        if self.getDistance(player.x, player.y) <= (player.radius + self.radius):
            return False
        else:
            return True

    def reset(self, x, y):
        self.x = x
        if self.winner == -1:
            self.x += 400
        if self.winner == 1:
            self.x -= 400
        self.y = y
        self.velocity = [0, 0]
        self.outsideHBounds = False
        self.outsideVBounds = False
        self.p1NotTouching = True
        self.p2NotTouching = True
        self.winner = 0

    def getDistance(self, px, py):
        return math.sqrt(math.pow((self.x-px), 2) + math.pow((self.y-py), 2))

    def getResultantVelocity(self, player):
        velBall = math.sqrt(math.pow(self.velocity[0], 2) + math.pow(self.velocity[1], 2))
        velPlayer = math.sqrt(math.pow(player.velx, 2) + math.pow(player.vely, 2))
        
        if player.velx != 0:
            playerAngle = math.atan(player.vely/player.velx)
            if player.velx < 0:
                playerAngle += math.pi
        else:
            playerAngle = math.asin(1)
            if player.vely < 0:
                playerAngle += math.pi

        contactAngle = math.atan((player.y - self.y)/(player.x - self.x))
        if player.x - self.x < 0:
            contactAngle += math.pi

        if self.velocity[0] != 0:
            ballVelAngle = math.atan(self.velocity[1]/self.velocity[0])
            if self.velocity[0] < 0:
                ballVelAngle += (math.pi)
        else:
            ballVelAngle = contactAngle
        


        resultAngle = 2*contactAngle - ballVelAngle + math.pi

        self.red = random.randint(0,255)
        self.green = random.randint(0,255)
        self.blue = random.randint(0,255)

        vx = velBall * math.cos(resultAngle) + player.absorber * velPlayer * math.cos(playerAngle) * player.mass/self.mass
        if vx > player.maxBallVel:
            vx = player.maxBallVel
        if vx < -1 * player.maxBallVel:
            vx = -1 * player.maxBallVel
        vy = velBall * math.sin(resultAngle) + player.absorber * velPlayer * math.sin(playerAngle) * player.mass/self.mass
        if vy > player.maxBallVel:
            vy = player.maxBallVel
        if vy < -1 * player.maxBallVel:
            vy = -1 * player.maxBallVel

        return [vx, vy]


