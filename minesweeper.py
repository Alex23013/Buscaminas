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

def make_maze(w=3, h=3):
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

def mine_counter(maze):
    aux = []
    for k in range(0, len(maze)):
        s1 = ''
        for l in range(0, len(maze[k])):
            cont = 0
            if maze[k][l] == '-':
                if k - 1 >= 0 and maze[k - 1][l] == '@':
                    cont += 1
                if k + 1 < len(maze) and maze[k + 1][l] == '@':
                    cont += 1
                if l - 1 >= 0 and maze[k][l - 1] == '@':
                    cont += 1
                if l + 1 < len(maze[k]) and maze[k][l + 1] == '@':
                    cont += 1
                if k - 1 >= 0 and l - 1 >= 0 and maze[k - 1][l - 1] == '@':
                    cont += 1
                if k + 1 < len(maze) and l + 1 < len(maze[k]) and maze[k + 1][
                            l + 1] == '@':
                    cont += 1
                if k - 1 >= 0 and l + 1 < len(maze[k]) and maze[k - 1][
                            l + 1] == '@':
                    cont += 1
                if k + 1 < len(maze) and l - 1 >= 0 and maze[k + 1][
                            l - 1] == '@':
                    cont += 1
                s1 += str(cont)
            else:
                s1 += str(maze[k][l])
        aux.append(s1)
    return aux


if __name__ == '__main__':
    maze = make_maze()
    for i in maze:
        print(i)

    maze_mines = mine_counter(maze)
    for i in maze_mines:
        print(i)

    serialized = maze_to_JSON(maze_mines)
