print("<-----RULES----->\n"
      "1. BRUSH DOWN\n"
      "2. BRUSH UP\n"
      "3. VEHICLE ROTATES RIGHT\n"
      "4. VEHICLE ROTATES LEFT\n"
      "5. MOVE UP TO X\n"
      "6. JUMP\n"
      "7. REVERSE DIRECTION\n"
      "8. VIEW THE MATRIX\n"
      "0. EXIT")
commands = input("Please enter the commands with a plus sign (+) between them.")
paint, direction, jump_count, row, column, matrix, move_count = 0, 1, 0, 1, 1, [], 0
loop, matrix_dimension, frame_count, check_count = 0, 0, 0, 0


def brush_position(x):
    global paint, row, matrix, column
    if int(x) == 1:
        paint = 1
        matrix[row][column] = "*"
    else:
        paint = 0


def car_direction(x):
    global direction
    if int(x) == 3:
        direction += 1
        direction = direction % 4
    elif int(x) == 4:
        direction += 3
        direction = direction % 4
    else:
        direction += 2
        direction = direction % 4


def keep_moving_vertical():  # when direction 0,2
    global column, row
    if row == 0:  # upward
        row = matrix_dimension - 2
    elif row == matrix_dimension - 1:
        row = 1


def keep_moving_horizontal():  # when direction 1, 3
    global column, row
    if column == 0:
        column = matrix_dimension - 2
    elif column == matrix_dimension - 1:
        column = 1


def jump():
    global jump_count, row, column, paint
    paint = 0
    while jump_count < 3:
        if direction == 0:
            row -= 1
            keep_moving_vertical()
            jump_count += 1
        elif direction == 1:
            column += 1
            keep_moving_horizontal()
            jump_count += 1
        elif direction == 2:
            row += 1
            keep_moving_vertical()
            jump_count += 1
        else:
            column -= 1
            keep_moving_horizontal()
            jump_count += 1
    jump_count = 0


def move(x):
    global move_count, row, column, matrix
    x = x.split("_")
    x = x[1]
    while move_count < int(x):
        if paint == 0:
            if direction == 0:
                row -= 1
                keep_moving_vertical()
                move_count += 1
            elif direction == 1:
                column += 1
                keep_moving_horizontal()
                move_count += 1
            elif direction == 2:
                row += 1
                keep_moving_vertical()
                move_count += 1
            else:
                column -= 1
                keep_moving_horizontal()
                move_count += 1
        elif paint == 1:
            if direction == 0:
                row -= 1
                keep_moving_vertical()
                move_count += 1
                matrix[row][column] = "*"

            elif direction == 1:
                column += 1
                keep_moving_horizontal()
                move_count += 1
                matrix[row][column] = "*"

            elif direction == 2:
                row += 1
                keep_moving_vertical()
                move_count += 1
                matrix[row][column] = "*"

            elif direction == 3:
                column -= 1
                keep_moving_horizontal()
                move_count += 1
                matrix[row][column] = "*"
    move_count = 0


def print_matrix():
    for i in range(matrix_dimension):
        for j in range(matrix_dimension):
            print(matrix[i][j], end="")
        print()


def matrix_func():
    global matrix_dimension, matrix
    for i in range(matrix_dimension):
        b = []
        for j in range(matrix_dimension):
            b.append(" ")
        matrix.append(b)


def frame():
    for a in range(matrix_dimension):
        for b in range(matrix_dimension):
            if a == 0 or b == matrix_dimension - 1 or a == matrix_dimension - 1 or b == 0:
                matrix[a][b] = "+"


def play():
    global paint, direction, jump_count, row, column, matrix, move_count, loop, matrix_dimension \
        , frame_count, commands, check_count
    commands = commands.split("+")
    matrix_dimension = int(commands[0]) + 2
    commands = commands[1:]
    matrix_func()
    while check_count != 1:
        for i in commands:
            if "_" in i:
                i = i.split("_")
                i = i[0]
                if int(i) > 8:
                    print("You entered an incorrect command. Please try again!")
                    commands = input()
                    commands = commands.split("+")
                    matrix_dimension = int(commands[0]) + 2
                    commands = commands[1:]
                    matrix_func()
                    check_count = 0
                    break
            elif int(i) > 8:
                print("You entered an incorrect command. Please try again!")
                commands = input()
                commands = commands.split("+")
                matrix_dimension = int(commands[0]) + 2
                commands = commands[1:]
                matrix_func()
                check_count = 0
                break
            else:
                check_count = 1
    frame()
    for i in commands:
        if int(i) == 1:
            brush_position(i)
        elif int(i) == 2:
            brush_position(i)
        elif int(i) == 3:
            car_direction(i)
        elif int(i) == 4:
            car_direction(i)
        elif int(i) == 7:
            car_direction(i)
        elif int(i) == 6:
            jump()
        elif "_" in i:
            move(i)
        elif int(i) == 8:
            print_matrix()
        elif int(i) == 0:
            break


play()
