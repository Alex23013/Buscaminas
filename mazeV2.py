from random import shuffle, randrange as rand

import json


def maze_to_JSON(maze):
    serialized = []
    for row in range(0, len(maze)):
        for col in range(0, len(maze[0])):
            serialized.append({'row': row,
                               'col': col,
                               'content': maze[row][col]})
    return json.dumps(serialized)


def maze(width=81, height=51, complexity=.75, density=.75):
    # Only odd shapes
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    density    = int(density * ((shape[0] // 2) * (shape[1] // 2)))
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
                y_,x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_][x_] == False:
                    Z[y_][x_] = True
                    Z[y_ + (y - y_) // 2][x_ + (x - x_) // 2] = True
                    x, y = x_, y_
    return Z

def check_mov(row,col,maze_mines,visible):
    aux = []
    if row - 1 >= 0 and visible[row-1][col]<2:
        aux.append((row-1,col))
    if row + 1 < len(maze_mines):
        if visible[row+1][col]<2:
            aux.append((row+1,col))
    if col - 1 >= 0 and visible[row][col-1]<2:
        aux.append((row,col-1))
    if col + 1 < len(maze_mines[0]) and visible[row][col+1]<2:
        aux.append((row,col+1))
    if row - 1 >= 0 and col - 1 >= 0 and visible[row-1][col-1]<2:
        aux.append((row-1,col-1))
    if row + 1 < len(maze_mines) and col + 1 < len(maze_mines) and visible[row+1][col+1]<2:
        aux.append((row+1,col+1))
    if col - 1 >= 0 and row + 1 <len(maze_mines) and visible[row+1][col-1]<2:
        aux.append((row+1,col-1))
    if col + 1 < len(maze_mines[0]) and row - 1 >= 0 and visible[row-1][col+1]<2:
        aux.append((row-1,col+1))
    return aux

def check_desb(row,col,maze_mines,visible):
    aux = []
    if row - 1 >= 0:
        aux.append((row-1,col))
    if row + 1 < len(maze_mines):
        aux.append((row+1,col))
    if col - 1 >= 0:
        aux.append((row,col-1))
    if col + 1 < len(maze_mines[0]):
        aux.append((row,col+1))
    if row - 1 >= 0 and col - 1 >= 0:
        aux.append((row-1,col-1))
    if row + 1 < len(maze_mines) and col + 1 < len(maze_mines):
        aux.append((row+1,col+1))
    if col - 1 >= 0 and row + 1 < len(maze_mines):
        aux.append((row+1,col-1))
    if col + 1 < len(maze_mines[0]) and row - 1 >= 0:
        aux.append((row-1,col+1))
    return aux

def watch(row, col,maze_mines, visible):
    if maze_mines[row][col] == 1:
        visible[row][col] = 1
    else :
        visible[row][col] = 0

def ifWin(maze):
    return maze[-2][-2] == 7

playerWon = False


if __name__ == '__main__':
    mz = maze(4,4)
    for i in mz:
        for j in i:
            if j :
                print("█",end='')
            else:
                print(" ", end= '')
        print()
    serialized = maze_to_JSON(mz)
    print (serialized)
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
        serial = maze_to_JSON(show)
        print (serial)
        if ifWin(show) :
            print("You Win =D")
            playerWon = True
            op = 2
            break
        print('\n')
        
        #for i in show:
        #    print(i)
        for i in show:
            for j in i:
                if j == 1 :
                    print("#",end='')
                elif j == 0:
                    print(" ", end= '')
                elif j == 7:
                    print("*", end= '')    
                else :
                    print("█",end='')
            print()
            
        op = int(input("What do you want to do?\n 0: move \t 1: unblock\t 2: quit Game\n"))
        if op == 0:
            aux = check_mov(posRow,posCol,mz,show)
            for i in range (0, len(aux)):
                print(str(i)+":"+str(aux[i]))
            if len(aux)>0:
                opt = int(input("What's your next mov? "))
                if(show[aux[opt][0]][aux[opt][1]]==0):
                    #print("Aqui")
                    (posRow, posCol) = aux[opt]
                else:
                    print("You cannot move to a wall!!")

            else:
                print("No hay opciones desbloqueadas")

        if op == 1:
            aux = check_desb(posRow,posCol,mz,show)
            for i in range (0, len(aux)):
                print(str(i)+":"+str(aux[i]))
            if len(aux)>0:
                opt = int(input("What's your option? ")) # todo :que solo pueda ingresar de las opciones ofrecidass (solo int) y no solo vacio
                (x, y) = aux[opt]
                watch(x,y,mz,show)
               
       
      
  
