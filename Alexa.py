import pygame
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Bird dimensions and initial position
BIRD_WIDTH = 50
BIRD_HEIGHT = 35
bird_x = 50
bird_y = int(SCREEN_HEIGHT / 2)

# Gravity and jump force
gravity = 0.25
jump_force = -6

# Pipe dimensions
PIPE_WIDTH = 70
PIPE_HEIGHT = random.randint(100, 400)
pipe_x = SCREEN_WIDTH

# Pipe gap
GAP_SIZE = 150
GAP_HEIGHT = random.randint(200, 400)

# Bird velocity
bird_velocity = 0

# Game over flag
game_over = False

# Score
score = 0
font = pygame.font.Font(None, 36)

# Load images
bird_img = pygame.image.load("bird.png")
bird_img = pygame.transform.scale(bird_img, (BIRD_WIDTH, BIRD_HEIGHT))
pipe_img = pygame.image.load("pipe.png")
pipe_img = pygame.transform.scale(pipe_img, (PIPE_WIDTH, PIPE_HEIGHT))

def display_score():
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

def display_bird(x, y):
    screen.blit(bird_img, (x, y))

def display_pipe(x, height):
    screen.blit(pipe_img, (x, 0))
    screen.blit(pipe_img, (x, height + GAP_SIZE))

def collision_detection(pipe_x, pipe_height):
    if bird_y < pipe_height or bird_y + BIRD_HEIGHT > pipe_height + GAP_SIZE:
        if pipe_x < bird_x + BIRD_WIDTH and bird_x < pipe_x + PIPE_WIDTH:
            return True
    return False

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bird_velocity = jump_force

    if not game_over:
        # Clear the screen
        screen.fill(BLACK)

        # Update bird position
        bird_velocity += gravity
        bird_y += bird_velocity

        # Update pipe position
        pipe_x -= 3

        # Check collision
        if collision_detection(pipe_x, PIPE_HEIGHT):
            game_over = True

        # Check if pipe passed the bird
        if pipe_x + PIPE_WIDTH < bird_x:
            score += 1
            PIPE_HEIGHT = random.randint(100, 400)
            pipe_x = SCREEN_WIDTH

        # Display bird and pipes
        display_pipe(pipe_x, PIPE_HEIGHT)
        display_bird(bird_x, bird_y)

        # Display score
        display_score()

        # Check if the bird touches the ground or goes above the screen
