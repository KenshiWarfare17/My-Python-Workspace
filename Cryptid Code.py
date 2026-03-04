import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mini GTA Python")

clock = pygame.time.Clock()

player = pygame.Rect(400, 300, 30, 30)
speed = 5
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player.y -= speed
    if keys[pygame.K_s]: player.y += speed
    if keys[pygame.K_a]: player.x -= speed
    if keys[pygame.K_d]: player.x += speed

    screen.fill((20, 20, 20))
    pygame.draw.rect(screen, (255, 50, 50), player)
    pygame.display.flip()

pygame.quit()
