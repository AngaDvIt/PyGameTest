import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello Pygame")

robot = pygame.image.load("robot.png")
# Set background color (red, blue, green)
backgroundColor = (50, 150, 200)


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(backgroundColor)
    screen.blit(robot, (100, 50))
    #Update game window
    pygame.display.flip()
# Quit Pygame
pygame.quit()


