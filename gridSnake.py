import random
import pygame
from pygame.locals import *

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 128, 0)

# Graphic dimensions
WIDTH = 600
HEIGHT = 600

# Board dimensions
COLUMN = 20
ROW = 20

# Dimensions of each square in the graphic
BOX_WIDTH = int((WIDTH / COLUMN))
BOX_HEIGHT = int((HEIGHT / ROW))

# Elements of the game (structure)
HEAD = '0'
BODY = 'X'
FOOD = '1'
EMPTY = ' '
score = 0

# Elements of the game (graphic)
head_skin = pygame.Surface((BOX_WIDTH, BOX_HEIGHT))
head_skin.fill(GREEN)

body_skin = pygame.Surface((BOX_WIDTH, BOX_HEIGHT))
body_skin.fill(DARK_GREEN)

food_skin = pygame.Surface((BOX_WIDTH, BOX_HEIGHT))
food_skin.fill(RED)

# Initializating elements of the game (structure)
snake = [[0, 0]] # snake[0] = the head; snake[1] = the body
food = [0, 0]
while food == snake[0]: # make sure food doesnt spawn in the same place that snake
    food = [random.randint(0, ROW - 1), random.randint(0, COLUMN - 1)]

board = [[EMPTY for i in range(COLUMN)] for j in range(ROW)]

# Positioning head and food
board[snake[0][0]][snake[0][1]] = HEAD
board[food[0]][food[1]] = FOOD

# Directions
RIGHT = 'RIGHT'
LEFT = 'LEFT'
UP = 'UP'
DOWN = 'DOWN'
my_direction = 'RIGHT'

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

def update(direction):
    global board, food, score

    if direction == RIGHT:
        # check snake collision
        if [snake[0][0], snake[0][1] + 1] in snake:
            pygame.quit()

        # Check if head collides with food
        if [snake[0][0], snake[0][1] + 1] == food:
            body = snake[0][:]
            snake.append(body)
            food = []
            score += 1
            while food == []:
                food = [random.randint(0, ROW - 1), random.randint(0, COLUMN - 1)]
                if food in snake:
                    food = []

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = [snake[i - 1][0], snake[i - 1][1]]

        snake[0][1] += 1

    if direction == LEFT:
        # Check if head collides with left border
        if snake[0][1] == 0:
            pygame.quit()

        if [snake[0][0], snake[0][1] - 1] in snake:
            pygame.quit()

        if [snake[0][0], snake[0][1] - 1] == food:
            body = snake[0][:]
            snake.append(body)
            food = []
            score += 1
            while food == []:
                food = [random.randint(0, ROW - 1), random.randint(0, COLUMN - 1)]
                if food in snake:
                    food = []

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = [snake[i - 1][0], snake[i - 1][1]]

        snake[0][1] -= 1

    if direction == UP:
        if snake[0][0] == 0:
            pygame.quit()

        if [snake[0][0] - 1, snake[0][1]] in snake:
            pygame.quit()

        if [snake[0][0] - 1, snake[0][1]] == food:
            body = snake[0][:]
            snake.append(body)
            food = []
            score += 1
            while food == []:
                food = [random.randint(0, ROW - 1), random.randint(0, COLUMN - 1)]
                if food in snake:
                    food = []

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = [snake[i - 1][0], snake[i - 1][1]]

        snake[0][0] -= 1

    if direction == DOWN:
        if [snake[0][0] + 1, snake[0][1]] in snake:
            pygame.quit()

        if [snake[0][0] + 1, snake[0][1]] == food:
            body = snake[0][:]
            snake.append(body)
            food = []
            score += 1
            while food == []:
                food = [random.randint(0, ROW - 1), random.randint(0, COLUMN - 1)]
                if food in snake:
                    food = []

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = [snake[i - 1][0], snake[i - 1][1]]

        snake[0][0] += 1

    board = [[EMPTY for i in range(COLUMN)] for j in range(ROW)]

    try:
        board[snake[0][0]][snake[0][1]] = HEAD
        if score > 0:
            for i in snake[1:]:
                board[i[0]][i[1]] = BODY
    except IndexError:
        pygame.quit()

    board[food[0]][food[1]] = FOOD

# Game Loop
while True:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()

            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP

            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN

            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT

            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT


    if my_direction == RIGHT:
        update(RIGHT)

    if my_direction == LEFT:
        update(LEFT)

    if my_direction == UP:
        update(UP)

    if my_direction == DOWN:
        update(DOWN)

    # Draw (graphic) the elements of the game
    screen.fill(BLACK)

    # Drawing based on the board (structure)
    for column in range(COLUMN):
        for row in range(ROW):
            if board[row][column] == HEAD:
                position = (column * BOX_WIDTH, row * BOX_HEIGHT)
                screen.blit(head_skin, position)

            elif board[row][column] == BODY:
                position = (column * BOX_WIDTH, row * BOX_HEIGHT)
                screen.blit(body_skin, position)

            elif board[row][column] == FOOD:
                position = (column * BOX_WIDTH, row * BOX_HEIGHT)
                screen.blit(food_skin, position)

    pygame.display.update()