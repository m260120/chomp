import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
blue = (0, 0, 255)
brown = (139, 69, 19)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blue Background with Brown Rectangle")

# create a surface
surf = pygame.Surface((50, 50))
# give the surface a color to separate it from the background
surf.fill((0, 0, 0))
rect = surf.get_rect()
surf_center = (screen_width/2 - surf.get_width()/2, screen_height/2 - surf.get_height()/2)
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Fill the screen with blue
    screen.fill(blue)
# Draw the brown rectangle at the bottom
    rectangle_height = 100
    pygame.draw.rect(screen, brown, (0, screen_height - rectangle_height, screen_width, rectangle_height))
    screen.blit(surf, surf_center)

# Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()