import random, pygame
from pygame.locals import *

def main():
    initialize_stuff()

    # Game loop
    while True:
        clock.tick(10)

        # Structure (move snake inside the grid)
        move()

        # Draw everything on the screen
        draw()

        # Update display
        pygame.display.update()

def move():
    global current_direction

    key = get_keyboard_input()
    if key == RIGHT and current_direction != LEFT:
        current_direction = key

    elif key == LEFT and current_direction != RIGHT:
        current_direction = key

    elif key == UP and current_direction != DOWN:
        current_direction = key

    elif key == DOWN and current_direction != UP:
        current_direction = key

    axis = AXIS[current_direction]
    step = MOVE[current_direction]

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = [snake[i - 1][0], snake[i - 1][1]]

    snake_head[axis] = (snake_head[axis] + step) % SIZE

    update()

def update():
    global board

    if valid_step():
        if snake_head == food:
            body = snake[-1][:]
            snake.append(body)
            spawn_food()

        board = [[" " for _ in range(SIZE)] for _ in range(SIZE)]
        board[snake_head[0]][snake_head[1]] = HEAD

        for body_part in snake[1:]:
            board[body_part[0]][body_part[1]] = BODY

        board[food[0]][food[1]] = FOOD
    else:
        pygame.quit()

def draw():
    # Draw (graphic) the elements of the game
    screen.fill(BLACK)

    # Drawing based on the board (structure)
    for column in range(SIZE):
        for row in range(SIZE):
            if board[row][column] == HEAD:
                position = (column * BOX_WIDTH, row * BOX_HEIGHT)
                screen.blit(head_skin, position)

            elif board[row][column] == BODY:
                position = (column * BOX_WIDTH, row * BOX_HEIGHT)
                screen.blit(body_skin, position)

            elif board[row][column] == FOOD:
                position = (column * BOX_WIDTH, row * BOX_HEIGHT)
                screen.blit(food_skin, position)

def valid_step():
    if snake_head in snake[1:]:
        return False
    return True

def spawn_food():
    global food
    food = []
    while food == []:
        food = [random.randint(0, SIZE - 1), random.randint(0, SIZE - 1)]
        if food in snake:
            food = []

def get_keyboard_input():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()

            if event.key == K_UP:
                return UP

            if event.key == K_DOWN:
                return DOWN

            if event.key == K_LEFT:
                return LEFT

            if event.key == K_RIGHT:
                return RIGHT

            if event.key == K_p:
                pause()

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_p:
                    paused = False

def initialize_stuff():
    global SIZE, HEAD, BODY, FOOD, snake_head, snake, food, board, RIGHT, LEFT, UP, DOWN, current_direction, MOVE, AXIS, RED, BLACK, GREEN, DARK_GREEN, \
        WIDTH, HEIGHT, BOX_WIDTH, BOX_HEIGHT, head_skin, body_skin, food_skin, clock, screen, paused

    # Board dimensions
    SIZE = 10

    # Elements of the game (structure)
    HEAD = 'X'
    BODY = 'O'
    FOOD = '8'

    # Initializating elements of the game (structure)
    snake_head = [0, 0]
    snake = [snake_head]
    food = [0, 0]
    spawn_food()
    board = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]

    # Directions
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'
    UP = 'UP'
    DOWN = 'DOWN'
    current_direction = RIGHT
    MOVE = {RIGHT: 1, LEFT: -1, UP: -1, DOWN: 1}
    AXIS = {RIGHT: 1, LEFT: 1, UP: 0, DOWN: 0}

    # Positioning head and food
    board[snake_head[0]][snake_head[1]] = HEAD
    board[food[0]][food[1]] = FOOD

    # Colors
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 128, 0)

    # Graphic dimensions
    WIDTH = 600
    HEIGHT = 600

    # Dimensions of each square in the graphic
    BOX_WIDTH = int((WIDTH / SIZE))
    BOX_HEIGHT = int((HEIGHT / SIZE))

    # Elements of the game (graphic)
    head_skin = pygame.Surface((BOX_WIDTH, BOX_HEIGHT))
    head_skin.fill(GREEN)

    body_skin = pygame.Surface((BOX_WIDTH, BOX_HEIGHT))
    body_skin.fill(DARK_GREEN)

    food_skin = pygame.Surface((BOX_WIDTH, BOX_HEIGHT))
    food_skin.fill(RED)

    # Pygame stuff
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()
    paused = False

main()