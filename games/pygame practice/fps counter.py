
"""
This program displays and fps counter.
Program stops when ESC is pressed.
"""

import pygame
pygame.init()  # Starts(initialises) pygame.

screen = pygame.display.set_mode((640,480))  # Set size of pygame window.
background = pygame.Surface(screen.get_size())  # Create empty pygame surface.
background.fill((255,255,255))  # Fill the background white color.
background = background.convert()  # Convert Surface object to make blitting faster.
screen.blit(background, (0,0))  # Copy background to screen (position (0, 0) is upper left corner).

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

pygame.quit()
print(f"Total playtime was: {playtime:.2f}")