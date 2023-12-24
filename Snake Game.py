import pygame
import time
import random

# Game setup
pygame.init()

width, height = 800, 600
snake_size = 50

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

white = (255, 255, 255)
red = (213, 50, 80)
black = (0, 0, 0)

clock = pygame.time.Clock()

font = pygame.font.SysFont("bahnschrift", 25)

# Function to draw snake
def draw_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_size, snake_size])

# Function to display message
def display_message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_size) / snake_size) * snake_size
    foody = round(random.randrange(0, height - snake_size) / snake_size) * snake_size

    while not game_over:

        while game_close == True:
            screen.fill(white)
            display_message("Game Over! Press Enter to play again or Esc to quit.", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_RETURN:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(white)
        pygame.draw.rect(screen, red, [foodx, foody, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_size, snake_list)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_size) / snake_size) * snake_size
            foody = round(random.randrange(0, height - snake_size) / snake_size) * snake_size
            length_of_snake += 1

        clock.tick(10)

    pygame.quit()
    quit()

game_loop()