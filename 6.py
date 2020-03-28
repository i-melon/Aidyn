import pygame

size = wight, height = (500, 500)
screen = pygame.display.set_mode(size)
pygame.init()

screen.fill((255, 255, 255))
for point in range(0,501,100):# range(start, stop, step)
    pygame.draw.line(screen, (point/2,point/2,point/2), (point, 0), (point, 500), 100)
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
pygame.quit()