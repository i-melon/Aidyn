import pygame

size = wight, height = (500, 500)
screen = pygame.display.set_mode(size)
pygame.init()

screen.fill((255, 255, 255))
# screen.fill(pygame.Color('black'), pygame.Rect(50,50,60,120))
# pygame.draw.circle(screen, (64, 128, 255), (250, 250), 200)
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
pygame.quit()