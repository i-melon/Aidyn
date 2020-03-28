import pygame

size = wight, height = (500, 500)
screen = pygame.display.set_mode(size)
pygame.init()

screen.fill((255, 255, 255))
pygame.draw.circle(screen, (230, 50, 230), (250, 250), 200)
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
pygame.quit()
