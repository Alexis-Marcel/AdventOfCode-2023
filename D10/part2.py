def parser():
    with open('input2.txt') as f:
        lines = f.readlines()
    return lines

#0 : droite, 1 : bas, 2 : gauche, 3 : haut
pipesMapConvert = { '-' : (0, 2), '|' : (1, 3), 'L' : (2, 1), 'F' : (3, 2), 'J' : (0, 1), '7' : (0, 3), 'S' : 'S', '.' : '(-1, -1)'}

#7-F7-
def parsePipes(lines):
    pipes = []
    for i in range(len(lines)):
        line = lines[i]
        # line to array
        line = line.strip()
        temp = list(line)
        if 'S' in temp:
            start = (i, temp.index('S'))
        pipes.append(temp)
    pipes[start[0]][start[1]] = replaceStart(pipes, start)
    return pipes, start

def invertDirection(direction):
    if direction == 0:
        return 2
    if direction == 1:
        return 3
    if direction == 2:
        return 0
    if direction == 3:
        return 1
    return -1

def directionToPosition(direction, position):
    (i, j) = position
    if direction == 0:
        return (i, j + 1)
    if direction == 1:
        return (i + 1, j)
    if direction == 2:
        return (i, j - 1)
    if direction == 3:
        return (i - 1, j)
    return (-1, -1)

def replaceStart(pipes, start):
    (i, j) = start
    n = len(pipes)
    m = len(pipes[0])
    
    directions = []
    
    for k in range(4):
        if k == 0 and j+1 < m and (pipesMapConvert[pipes[i][j + 1]][0] == k or pipesMapConvert[pipes[i][j + 1]][1] == k):
            directions.append(invertDirection(k))
        if k == 1 and i+1 < n and (pipesMapConvert[pipes[i + 1][j]][0] == k or pipesMapConvert[pipes[i + 1][j]][1] == k):
            directions.append(invertDirection(k))
        if k == 2 and j-1 >= 0 and (pipesMapConvert[pipes[i][j - 1]][0] == k or pipesMapConvert[pipes[i][j - 1]][1] == k):
            directions.append(invertDirection(k))
        if k == 3 and i-1 >= 0 and (pipesMapConvert[pipes[i - 1][j]][0] == k or pipesMapConvert[pipes[i - 1][j]][1] == k):
            directions.append(invertDirection(k))
            
    for key in pipesMapConvert:
        if pipesMapConvert[key] == tuple(directions) or pipesMapConvert[key] == tuple(directions[::-1]):
            return key
    
    
 
def findNextDirection(pipes, position, direction):
    (i, j) = position
    (d1, d2) = pipesMapConvert[pipes[i][j]]
    if direction == d1:
        return invertDirection(d2)
    else:
        return invertDirection(d1)
    
def is_inside_loop(grid, point):
    i, j = point
    crossings = 0
    k=j
    while k < len(grid[0]) :
        if grid[i][k] == '.':
            k += 1
            continue
        if grid[i][k] == '|':
            crossings += 1
            k += 1
            continue
        first = grid[i][k]
        k += 1
        while k < len(grid[0]) and grid[i][k] == '-':
            k += 1
        last = grid[i][k]
        if (first == 'L' and last == 'J') or (first == 'F' and last == '7'):
            k += 1
            continue
        crossings += 1
        k+=1
                
    return crossings % 2 != 0

def find_inner_points(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not grid[i][j] != '.' and is_inside_loop(grid, (i, j)):
                count += 1
    return count

    
def main():
    lines = parser()
    
    (pipes, start) = parsePipes(lines)
    
    position = start
    direction = pipesMapConvert[pipes[start[0]][start[1]]][0]
        
    perimeter = 1
    
    isLoop = [['.' for i in range(len(pipes[0]))] for j in range(len(pipes))]
    
    isLoop[start[0]][start[1]] = pipes[start[0]][start[1]]

    while position != start or perimeter == 1:

        (i, j) = position
        newDirection = findNextDirection(pipes, position, direction)        

        position = directionToPosition(newDirection, (i, j))
        direction = newDirection
        
        perimeter += 1
        isLoop[i][j] = pipes[i][j]
    
    print(perimeter)
    
    print(find_inner_points(isLoop))
                            
                             
main()

