import pygame
import Game
import Players
import Ball

pygame.init()
game = Game.gameFrame(1920, 1080)
surface = game.getSurface()
outline = Game.Outline()
player1 = Players.PlayerLeft(120, 560)
player2 = Players.PlayerRight(1680, 560)
ball = Ball.Ball(900, 560)
clock = pygame.time.Clock()
scoreboard = Game.Score()

running = True
while running:
    dt = clock.tick(120)
    pygame.Surface.fill(surface, pygame.Color(0,0,0))
    ball.move(player1, player2, dt)
    ball.draw(surface)
    outline.draw(surface)
    player1.move(dt, player2)
    player1.draw(surface)
    player2.move(dt, player1)
    player2.draw(surface)
    scoreboard.updateScore(surface, ball.winner)
    if ball.winner != 0:
        ball.reset(900, 505)
        player1.reset(190, 505)
        player2.reset(1680, 505)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
  
  
pygame.quit()

