import pygame

size = wight, height = (500, 500)
screen = pygame.display.set_mode(size)
pygame.init()

screen.fill((255, 255, 255))
for point in range(0,641,64): # range(start, stop, step)
   pygame.draw.line(screen, (255,0,255), (0,0), (500, point), 1)
   pygame.draw.line(screen, (255,0,255), (500,0), (0, point), 1)
   pygame.draw.line(screen, (255, 0, 255), (0, 500), (500, point), 1)
   pygame.draw.line(screen, (255, 0, 255), (500, 500), (0, point), 1)
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
pygame.quit()