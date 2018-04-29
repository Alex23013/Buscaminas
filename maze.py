from random import randrange as rand
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

mz = maze(10,10)
# density = 2
for i in mz:
    for j in i:
        if j :
            print("█",end='')
        else:
            print(" ", end= '')
    print()
