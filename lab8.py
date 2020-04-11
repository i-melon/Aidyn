import pygame

size = wight, height = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("The Ball")
pygame.init()

screen.fill((255, 255, 255))
x = 25
y = 475
speed = 20

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x >25:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 675:
        x += speed
    if keys[pygame.K_UP] and y > 25:
        y -= speed
    if keys[pygame.K_DOWN] and y < 475:
        y += speed
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255,0,0), (x, y), 25)
    pygame.display.update()


pygame.quit()