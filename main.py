import pygame, random

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
x, y = 300, 200
vx, vy = 3, 2
reloj = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

    x += vx
    y += vy

    if random.random() < 0.05:
        vx = random.randint(-5, 5)
        vy = random.randint(-5, 5)

    pantalla.fill((0, 0, 0))
    pygame.draw.circle(pantalla, (0, 255, 100), (x, y), 20)
    pygame.display.flip()
    reloj.tick(60)