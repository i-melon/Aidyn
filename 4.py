import pygame

size = wight, height = (500, 500)
screen = pygame.display.set_mode(size)
pygame.init()

screen.fill((255, 255, 255))
pi = 3,14
pygame.draw.circle(screen, (0,0,0), (0,250), 250)
pygame.draw.circle(screen, (255,255,255), (0,250), 245)
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
pygame.quit()