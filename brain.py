import pygame, random, string

pygame.init()
screen = pygame.display.set_mode((400, 250))
pygame.display.set_caption("Mini Brain 🧠")

font = pygame.font.SysFont("monospace", 55)
letter = "A"
last_time = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if pygame.time.get_ticks() - last_time >= 1000:
        letter = random.choice(string.ascii_uppercase)
        last_time = pygame.time.get_ticks()

    screen.fill((15, 15, 25))
    text = font.render(letter, True, (0, 255, 120))
    screen.blit(text, text.get_rect(center=(200, 125)))

    pygame.display.flip()
    clock.tick(60)