# gridSnake
This project is an implementation of the game snake using python and pycharm. It's splitted into two parts: structural 
and graphical.

# The project
All the logic of the game is in the 'structural' part. There is a 2D-array to keep track of the board, and all the 
movements and check are made with this grid.
For example, this piece of code checks the collision between the snake and the food and keep sure
to spawn the food in a free slot:

        if [snake[0][0], snake[0][1] + 1] == food:
            body = snake[0][:]
            snake.append(body)
            food = []
            score += 1
            while food == []:
                food = [random.randint(0, ROW - 1), random.randint(0, COLUMN - 1)]
                if food in snake:
                    food = []
                    


While the following code makes the 'body' of the snake follow the 'head':

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = [snake[i - 1][0], snake[i - 1][1]]
         
The code uses the game loop to update the movement of the snake in the grid and in the GUI.


    While True:
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
        
And finally, here is the piece of code to draw everything. All the code before this  refers to the structural part.

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
