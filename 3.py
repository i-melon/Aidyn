import pygame

size = wight, height = (500, 500)
screen = pygame.display.set_mode(size)
pygame.init()

screen.fill((255, 255, 255))
pygame.draw.polygon(screen, (0,0,0), [[250,50], [250,60], [375,460], [375,450]])
pygame.draw.polygon(screen, (0,0,0), [[50,190], [50,200], [375,460], [375,450]])
pygame.draw.polygon(screen, (0,0,0), [[50,190], [50,200], [450,200], [450,190]])
pygame.draw.polygon(screen, (0,0,0), [[125,450], [125,460], [450,200], [450,190]])
pygame.draw.polygon(screen, (0,0,0), [[125,450], [125,460], [250,60], [250,50]])
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
pygame.quit()