from random import shuffle, randrange
import json


def maze_to_JSON(maze):
    serialized = []
    for row in range(0, len(maze)):
        for col in range(0, len(maze[0])):
            serialized.append({'row': row,
                               'col': col,
                               'content': maze[row][col]})
    return json.dumps(serialized)

def make_maze(w=5, h=5): # largo = h*2-1
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [['@-'] * w + ['@'] for _ in range(h)] + [[]]
    hor = [['@@'] * w + ['@'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = '@-'
            if yy == y: ver[y][max(x, xx)] = '--'
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    maze = []
    for (a, b) in zip(hor, ver):
        maze.append(''.join(a)[1:-1])
        maze.append(''.join(b)[1:-1])

    return maze[1:-2]

def check_mov(row,col,maze_mines):
    aux = []
    if row - 1 >= 0 and maze_mines[row - 1][col] != '@':
        aux.append((row-1,col))
    if row + 1 <= len(maze_mines) and maze_mines[row + 1][col] != '@':
        aux.append((row+1,col))
    if col - 1 >= 0 and maze_mines[row][col-1] != '@':
        aux.append((row,col-1))
    if col + 1 <= len(maze_mines[0]) and maze_mines[row][col+1] != '@':
        aux.append((row,col+1))
    if row - 1 >= 0 and col - 1 >= 0  and maze_mines[row - 1][col -1] != '@':
        aux.append((row-1,col-1))
    if row + 1 <= len(maze_mines) and col + 1 <= len(maze_mines) and maze_mines[row + 1][col+1] != '@':
        aux.append((row+1,col+1))
    if col - 1 >= 0 and row + 1 <= len(maze_mines) and  maze_mines[row+1][col-1] != '@':
        aux.append((row,col-1))
    if col + 1 <= len(maze_mines[0]) and row - 1 >= 0 and maze_mines[row-1][col+1] != '@':
        aux.append((row,col+1))
    return aux
 
def watch(row, col,maze_mines, visible):
    if maze_mines[row][col] == '@':
        visible[row][col] = 1
    else :
        visible[row][col] = 2


playerWon = False


if __name__ == '__main__':
     
    maze = make_maze()
    for i in maze:
        print(i)

    serialized = maze_to_JSON(maze)
    
    show = []
    for row in range(0, len(maze)):
        show.append([])
        for col in range(0, len(maze[0])):
            show[row].append(0)
    posRow, posCol = 0, 0
    op = 0
    while playerWon == False and op != 2:
        print('\n')
        show[posRow][posCol] = 8
        for i in show:
            print(i)
        op = input("What do you want to do\n 0: move \t 1: unblock\t 2: quit Game\n")
        if op == 0:
            aux = check_mov(posRow,posCol,maze)
            print(aux)
            opt = input("What's your next mov? ")
            (posRow, posCol) = aux[opt-1]
            if posRow == 0 and posCol == 8:
                playerWon = True
                op = 2
        if op == 1:
            x = input("x?: ")
            y = input("y?: ")
            watch(x,y,maze,show)
         
       
      
  
