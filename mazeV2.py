from random import randrange as rand
import json


def generate_maze_visible(rows, cols):
    '''
    Returns: a tuple containing the generated maze and the visibility matrix.
    '''
    maze = generate_maze(rows, cols)
    visible = [[False] * len(maze[0]) for i in range(len(maze))]
    return (maze, visible)

def matrix_to_JSON(matrix):
    serialized = []
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            serialized.append({'row': row,
                               'col': col,
                               'content': matrix[row][col]})
    return json.dumps(serialized)

def validate_mov(current_row, current_col, next_row, next_col, maze_vis):
    '''
    Returns: True if the next move (next_row and next_col) is valid.
    '''
    row_size = len(maze_vis[0])
    col_size = len(maze_vis[0][0])

    # Check boundaries
    if next_row < 1 or next_row >= row_size - 1:
        return False
    if next_col < 1 or next_col >= col_size - 1:
        return False

    # Check that the next position is adjacent to the current position
    row_diff = next_row - current_row
    col_diff = next_col - current_col
    if row_diff not in (-1, 0, 1):
        return False
    if col_diff not in (-1, 0, 1):
        return False

    # Check that the next position square is visible:
    if not maze_vis[1][next_row][next_col]:
        return False

    # Check that the next position square is not a wall:
    if maze_vis[0][next_row][next_col]:
        return False

    return True

def validate_unlock(target_row, target_col, maze_vis):
    '''
    Returns: True if the target square (target_row, target_col) is unlockable.
    '''
    row_size = len(maze_vis[0])
    col_size = len(maze_vis[0][0])

    # Check boundaries
    if target_row < 0 or target_row >= row_size:
        return False
    if target_row < 0 or target_row >= col_size:
        return False

    # Check adjacent visible squares
    if target_row - 1 >= 0:
        if target_col - 1 >= 0 and maze_vis[1][target_row - 1][target_col - 1]:
            return True
        if maze_vis[1][target_row - 1][target_col]:
            return True
        if (target_col + 1 < row_size and
                maze_vis[1][target_row - 1][target_col + 1]):
            return True
    if target_col - 1 >= 0 and maze_vis[1][target_row][target_col - 1]:
        return True
    if target_col + 1 < row_size and maze_vis[1][target_row][target_col + 1]:
        return True
    if target_row + 1 < row_size:
        if target_col - 1 >= 0 and maze_vis[1][target_row + 1][target_col - 1]:
            return True
        if maze_vis[1][target_row + 1][target_col]:
            return True
        if (target_col + 1 < row_size and
                maze_vis[1][target_row + 1][target_col + 1]):
            return True

    return False

def check_win(pos_row, pos_col, maze_vis):
    '''
    Returns: True if the player win in the position (pos_row, pos_col).
    '''
    row_size = len(maze_vis[0])
    col_size = len(maze_vis[0][0])

    # Check that the goal square is visible
    if not maze_vis[1][-2][-2]:
        return False

    # Check that the position is the same as the goal position
    if pos_row == row_size - 2 and pos_col == col_size - 2:
        return True

    return False

def generate_maze(width=81, height=51, complexity=.75, density=.75):
    # Only odd shapes
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    density = int(density * ((shape[0] // 2) * (shape[1] // 2)))
    # Build actual maze
    Z = [[False] * shape[1] for i in range(shape[0])]
    # Fill borders
    Z[0] = Z[-1] = [True] * shape[1]
    for i in range(len(Z)):
        Z[i][0] = True
        Z[i][-1] = True
    # Make aisles
    for i in range(density):
        x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2
        Z[y][x] = True
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_, x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_][x_] == False:
                    Z[y_][x_] = True
                    Z[y_ + (y - y_) // 2][x_ + (x - x_) // 2] = True
                    x, y = x_, y_
    return Z


################################

def check_mov(row, col, maze, visible):
    aux = []
    if row - 1 >= 0 and visible[row - 1][col] < 2:
        aux.append((row - 1, col))
    if row + 1 < len(maze):
        if visible[row + 1][col] < 2:
            aux.append((row + 1, col))
    if col - 1 >= 0 and visible[row][col - 1] < 2:
        aux.append((row, col - 1))
    if col + 1 < len(maze[0]) and visible[row][col + 1] < 2:
        aux.append((row, col + 1))
    if row - 1 >= 0 and col - 1 >= 0 and visible[row - 1][col - 1] < 2:
        aux.append((row - 1, col - 1))
    if row + 1 < len(maze) and col + 1 < len(maze) and visible[row + 1][
                col + 1] < 2:
        aux.append((row + 1, col + 1))
    if col - 1 >= 0 and row + 1 < len(maze) and visible[row + 1][
                col - 1] < 2:
        aux.append((row + 1, col - 1))
    if col + 1 < len(maze[0]) and row - 1 >= 0 and visible[row - 1][
                col + 1] < 2:
        aux.append((row - 1, col + 1))
    return aux

def check_visible(row, col, maze, visible):
    aux = []
    if row - 1 >= 0:
        aux.append((row - 1, col))
    if row + 1 < len(maze):
        aux.append((row + 1, col))
    if col - 1 >= 0:
        aux.append((row, col - 1))
    if col + 1 < len(maze[0]):
        aux.append((row, col + 1))
    if row - 1 >= 0 and col - 1 >= 0:
        aux.append((row - 1, col - 1))
    if row + 1 < len(maze) and col + 1 < len(maze):
        aux.append((row + 1, col + 1))
    if col - 1 >= 0 and row + 1 < len(maze):
        aux.append((row + 1, col - 1))
    if col + 1 < len(maze[0]) and row - 1 >= 0:
        aux.append((row - 1, col + 1))
    return aux

def watch(row, col, maze_mines, visible):
    if maze_mines[row][col] == 1:
        visible[row][col] = 1
    else:
        visible[row][col] = 0

def check_win(maze):
    return maze[-2][-2] == 7

def print_visible(show):
    for i in show:
        for j in i:
            if j == 1:
                print("#", end='')
            elif j == 0:
                print(" ", end='')
            elif j == 7:
                print("*", end='')
            else:
                print("█", end='')
        print()

def print_maze(maze):
    for i in maze:
        for j in i:
            if j:
                print("█", end='')
            else:
                print(" ", end='')
        print()

playerWon = False

if __name__ == '__main__':
    mz = generate_maze(4, 4)
    for i in mz:
        for j in i:
            if j:
                print("█", end='')
            else:
                print(" ", end='')
        print()
    serialized = matrix_to_JSON(mz)
    print(serialized)
    show = []
    for row in range(0, len(mz)):
        show.append([])
        for col in range(0, len(mz[0])):
            show[row].append(2)
    posRow, posCol = 1, 1
    op = 0
    # 0 no desbloqueado
    # 1 desbloqueado pared
    # 2 desbloqueado libre
    while playerWon == False and op != 2:
        print(op)
        show[posRow][posCol] = 7
        serial = matrix_to_JSON(show)
        print(serial)
        if check_win(show):
            print("You Win =D")
            playerWon = True
            op = 2
            break
        print('\n')

        # for i in show:
        #    print(i)
        print_visible(show)
        op = int(input(
            "What do you want to do?\n 0: move \t 1: unblock\t 2: quit Game\n"))
        if op == 0:
            aux = check_mov(posRow, posCol, mz, show)
            for i in range(0, len(aux)):
                print(str(i) + ":" + str(aux[i]))
            if len(aux) > 0:
                opt = int(input("What's your next mov? "))
                if (show[aux[opt][0]][aux[opt][1]] == 0):
                    # print("Aqui")
                    (posRow, posCol) = aux[opt]
                else:
                    print("You cannot move to a wall!!")

            else:
                print("No hay opciones desbloqueadas")

        if op == 1:
            aux = check_visible(posRow, posCol, mz, show)
            for i in range(0, len(aux)):
                print(str(i) + ":" + str(aux[i]))
            if len(aux) > 0:
                opt = int(input(
                    "What's your option? "))  # todo :que solo pueda ingresar de las opciones ofrecidass (solo int) y no solo vacio
                (x, y) = aux[opt]
                watch(x, y, mz, show)
