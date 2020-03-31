import  sys
import pygame

pygame.init()
size=width,height=640,480
screen=pygame.display.set_mode(size)
color=(0,0,0)
ball=pygame.image.load("a.jpg")
ballrect=ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    screen.fill(color)
    screen.blit(ball,ballrect)
    pygame.display.flip()

pygame.quit()