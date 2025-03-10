import pygame
import math
# Set up the screen
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Grid Map')

# Define grid dimensions and colors
rows, cols = 10, 10
grid_size = 40
grid_color = (200, 200, 200)
line_color = (0, 0, 0)

# Create a grid of rectangles
for row in range(rows):
    for col in range(cols):
        pygame.draw.rect(screen, grid_color, (col * grid_size, row * grid_size, grid_size, grid_size))
        pygame.draw.rect(screen, line_color, (col * grid_size, row * grid_size, grid_size, grid_size), 1)

pygame.display.flip()

# Run the Pygame loop to display the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
