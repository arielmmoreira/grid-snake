# Grid Snake
This project is an implementation of the game snake using python and pycharm. It's divided into two parts: structural 
and graphical.

# The project
The main goal of this project is to study some structures and algorithms.

All the logic of the game is in the 'structural' part. There is a 2D-array to keep track of the board, and all the 
movements and check are made with this grid.

For example, this piece of code updates all the structure of the game. Checks if it's a valid step, if the snake eat the food and update a grid with elements inside.

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
                    


While the following code makes the 'body' of the snake follow the 'head':

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = [snake[i - 1][0], snake[i - 1][1]]
  
         
         
This is the main function, and it's possible to have an overview of the project.


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
    
        
And finally, here is the piece of code to draw everything. All the code before this  refers to the structural part.

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

