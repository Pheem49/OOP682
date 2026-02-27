import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
ruuning = True
sara_sheet = pygame.image.load('sara/sara-cal1.png')
sara_rect = pygame.Rect(0, 0, 34, 56)
sara_pos = pygame.Rect(50, 50, 34, 56)
clock = pygame.time.Clock()
while ruuning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ruuning = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and sara_pos.x > 0:
        sara_pos.x -= 5
    elif key[pygame.K_RIGHT] and sara_pos.x + sara_pos.width < 400:
        sara_pos.x += 5
    elif key[pygame.K_UP] and sara_pos.y > 0:
        sara_pos.y -= 5
    elif key[pygame.K_DOWN] and sara_pos.y + sara_pos.height < 300:
        sara_pos.y += 5
    clock.tick(90)
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont('Arial', 30)
    text = font.render(f"{clock.get_fps():.2f} FPS", True, (0, 0, 0))
    screen.blit(text, (150, 230))
    screen.blit(sara_sheet, (sara_pos.x, sara_pos.y), sara_rect)
    pygame.display.update()
pygame.quit()
    