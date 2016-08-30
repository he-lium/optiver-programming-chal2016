
row, col = [int(i) for i in input().split()]
grid = list()
unlit = list()

for r in range(row):
    grid.append(list(input()))
    for c in range(col):
        if grid[r][c] == '.':
            unlit.append((r, c))

def place_bulb(r, c):
    print (r,c)
    grid[r][c] = '@'
    unlit.remove((r,c))
    # left
    i = r-1
    while i >= 0:
        if grid[i][c] != '.':
            break
        if (i, c) in unlit:
            unlit.remove((i, c))
        i -= 1
    # right
    i = r+1
    while i < row:
        if grid[i][c] != '.':
            break
        if (i, c) in unlit:
            unlit.remove((i, c))
        i += 1
    # up
    i = c-1
    while i >= 0:
        if grid[r][i] != '.':
            break
        if (r, i) in unlit:
            unlit.remove((r, i))
        i -= 1
    # down
    i = c+1
    while i >= col:
        if grid[r][i] != '.':
            break
        if (r, i) in unlit:
            unlit.remove((r, i))
        i += 1

def adj(r, c):
    result = list()
    if r > 0: result.append((r-1,c))
    if c > 0: result.append((r,c-1))
    if r < row-1: result.append((r+1,c))
    if c < col-1: result.append((r,c+1))
    return result
#while (len(unlit) > 0):

for r in range(row):
    for c in range(col):
        if grid[r][c].isdigit():
            count = int(grid[r][c])
            adjacents = adj(r, c)
            adjacents = [coord for coord in adjacents if coord in unlit]
            if len(adjacents) <= count:
                for coord in adjacents:
                    place_bulb(coord[0], coord[1])

print('\n'.join([''.join(r) for r in grid]))
print(unlit)
