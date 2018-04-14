from random import shuffle, randrange
 
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
 
if __name__ == '__main__':
    maze,maze1 = make_maze()
    for i in maze:
        print(i) 
    for j in maze1:
        print j 
    maze2 = maze1[1:-2]
    aux=[]
    for k in range(0,len(maze2)):
        
        s1=""
        for l in range(0, len(maze2[k])):
            cont = 0
            if maze2[k][l] == "-":
                if k-1>=0 and maze2[k-1][l]=="@":
                    cont+=1
                if k+1<len(maze2) and maze2[k+1][l]=="@":
                    cont+=1
                if l-1>=0 and maze2[k][l-1]=="@":
                    cont+=1
                if l+1<len(maze2[k]) and maze2[k][l+1]=="@":
                    cont+=1
                if k-1>=0 and l-1>=0 and maze2[k-1][l-1]=="@":
                    cont+=1
                if k+1<len(maze2) and l+1<len(maze2[k]) and maze2[k+1][l+1]=="@":
                    cont+=1
                if k-1>=0 and l+1<len(maze2[k]) and maze2[k-1][l+1]=="@":
                    cont+=1
                if k+1<len(maze2) and l-1>=0 and maze2[k+1][l-1]=="@":
                    cont+=1
                s1+= str(cont)
            else:
                s1+=str(maze2[k][l])
        aux.append(s1)
    for j in aux:
        print j
