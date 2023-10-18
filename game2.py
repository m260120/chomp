import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

# # Colors
# blue = (0, 0, 255)
# brown = (139, 69, 19)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Using tiles and blit to draw on a surface")

# # create a surface
# surf = pygame.Surface((50, 50))
# # give the surface a color to separate it from the background
# surf.fill((0, 0, 0))
# rect = surf.get_rect()
# surf_center = (screen_width/2 - surf.get_width()/2, screen_height/2 - surf.get_height()/2)

# Load tiles from assets.zip into surfaces
water = pygame.image.load("assets/sprites/water.png").convert()
sand = pygame.image.load("assets/sprites/sand.png").convert()
seagrass = pygame.image.load("assets/sprites/seagrass.png").convert()
# use png transparancey
sand.set_colorkey((0,0,0))
water.set_colorkey((0,0,0))
seagrass.set_colorkey((0,0,0))
# fill screen with water
for x in range(0, screen_width, tile_size):
    for y in range(0, screen_height, tile_size):
        screen.blit(water, (x, y))
for x in range(0, screen_width, tile_size):
    for y in range(screen_height, screen_height-65, -tile_size):
        screen.blit(sand, (x,y))
for x in range(0, 3):
    position_x = random.randint(0, 800)
    position_y = screen_height - tile_size*1.80
    screen.blit(seagrass, (position_x, position_y))
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(screen, (0,0))
    pygame.display.flip()
# # Fill the screen with blue
#     screen.fill(blue)
# # Draw the brown rectangle at the bottom
#     rectangle_height = 100
#     pygame.draw.rect(screen, brown, (0, screen_height - rectangle_height, screen_width, rectangle_height))
#     screen.blit(surf, surf_center)

# Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()