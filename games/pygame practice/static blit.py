import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))
background = background.convert()

ballsurface = pygame.Surface((50,50))
pygame.draw.circle(ballsurface, (0,0,255), (25,25), 25)
ballsurface = ballsurface.convert()
ballx = 320
bally = 240

screen.blit(background, (0,0))
screen.blit(ballsurface, (ballx, bally))
mainloop = True

clock = pygame.time.Clock()
playtime = 0.0

while mainloop:
    milliseconds = clock.tick(30)
    playtime += milliseconds / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False

    text = f"FPS: {clock.get_fps():.2f}  Playtime: {playtime:.2f}"
    pygame.display.set_caption(text)
    pygame.display.flip()

pygame.quit()
print(f"Total playtime was: {playtime:.2f}")