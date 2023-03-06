import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 480
screen_height = 480
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Set up the font
font = pygame.font.SysFont(None, 25)

# Set up the clock
clock = pygame.time.Clock()

# Set up the snake and food
block_size = 10
snake_speed = 15

def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(game_window, green, [block[0], block[1], snake_block, snake_block])

def message(msg, color):
    message_text = font.render(msg, True, color)
    game_window.blit(message_text, [screen_width/6, screen_height/3])

def game_loop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            game_window.fill(white)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_window.fill(white)
        pygame.draw.rect(game_window, red, [foodx, foody, block_size, block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)

        pygame.display.update()

       
