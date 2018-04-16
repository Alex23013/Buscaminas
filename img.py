from random import shuffle, randrange

def make_mazeNN(w = 3, h = 3):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["@-"] * w + ['@'] for _ in range(h)] + [[]]
    hor = [["@@"] * w + ['@'] for _ in range(h + 1)]
 
    w = []
    for (a, b) in zip(hor, ver):
        w.append(''.join(a))
        w.append(''.join(b))  
       
    return w
 
 
def make_maze(w = 3, h = 3):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["@-"] * w + ['@'] for _ in range(h)] + [[]]
    hor = [["@@"] * w + ['@'] for _ in range(h + 1)]
 
    def walk(x, y):
        vis[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "@-"
            if yy == y: ver[y][max(x, xx)] = "--"
            walk(xx, yy)
 
    walk(randrange(w), randrange(h))
 
    s = []
    for (a, b) in zip(hor, ver):
        s.append(''.join(a))
        s.append(''.join(b))  
    
    w = []
    for (a, b) in zip(hor, ver):
        w.append(''.join(a)[1:-1])
        w.append(''.join(b)[1:-1])  
    
       
    return s,w
 
def mineCounter(maze):
    aux=[]
    for k in range(0,len(maze)):
        s1=""
        for l in range(0, len(maze[k])):
            cont = 0
            if maze[k][l] == "-":
                if k-1>=0 and maze[k-1][l]=="@":
                    cont+=1
                if k+1<len(maze) and maze[k+1][l]=="@":
                    cont+=1
                if l-1>=0 and maze[k][l-1]=="@":
                    cont+=1
                if l+1<len(maze[k]) and maze[k][l+1]=="@":
                    cont+=1
                if k-1>=0 and l-1>=0 and maze[k-1][l-1]=="@":
                    cont+=1
                if k+1<len(maze) and l+1<len(maze[k]) and maze[k+1][l+1]=="@":
                    cont+=1
                if k-1>=0 and l+1<len(maze[k]) and maze[k-1][l+1]=="@":
                    cont+=1
                if k+1<len(maze) and l-1>=0 and maze[k+1][l-1]=="@":
                    cont+=1
                s1+= str(cont)
            else:
                s1+=str(maze[k][l])
        aux.append(s1)
    return aux


if __name__ == '__main__':
    maze3 = make_mazeNN();
    for i in maze3:
        print(i)

    maze,maze1 = make_maze()
    for i in maze:
        print(i) 
    for j in maze1:
        print(j)
    maze2 = maze1[1:-2]

    aux = mineCounter(maze2)
    for j in aux:
        print(j)
