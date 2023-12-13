def parser():
    with open('input2.txt') as f:
        lines = f.readlines()
    return lines

#0 : droite, 1 : bas, 2 : gauche, 3 : haut
pipesMapConvert = { '-' : (0, 2), '|' : (1, 3), 'L' : (2, 1), 'F' : (3, 2), 'J' : (0, 1), '7' : (0, 3), '.' : (-1, -1)}

#7-F7-
def parsePipes(lines):
    pipes = []
    for i in range(len(lines)):
        line = lines[i]
        line = line.strip()
        temp = []
        for j in range(len(line)):
            if line[j] == 'S':
                start = (i, j)
                temp.append((-1, -1))
            else:
                temp.append(pipesMapConvert[line[j]])
        pipes.append(temp)
    pipes[start[0]][start[1]] = findStartDirections(pipes, start)
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

def findStartDirections(pipes, start):
    (i, j) = start
    n = len(pipes)
    m = len(pipes[0])
    
    directions = []
    
    for k in range(4):
        if k == 0 and (j + 1 > m or not (pipes[i][j + 1][0] == k or pipes[i][j + 1][1] == k)):
            continue
        if k == 1 and (i + 1 > n or not (pipes[i + 1][j][0] == k or pipes[i + 1][j][1] == k)):
            continue
        if k == 2 and (j - 1 < 0 or not (pipes[i][j - 1][0] == k or pipes[i][j - 1][1] == k)):
            continue
        if k == 3 and (i - 1 < 0 or not (pipes[i - 1][j][0] == k or pipes[i - 1][j][1] == k)):
            continue
        directions.append(invertDirection(k))
    return (directions[0], directions[1])
 
def findNextDirection(pipes, position, direction):
    (i, j) = position
    if pipes[i][j][0] == direction:
        return invertDirection(pipes[i][j][1])
    return invertDirection(pipes[i][j][0])
        
def main():
    lines = parser()
    
    (pipes, start) = parsePipes(lines)
    
    position = start
    if pipes[start[0]][start[1]][0] == 3 or pipes[start[0]][start[1]][0] == 0:
        direction = pipes[start[0]][start[1]][0]
    else:
        direction = pipes[start[0]][start[1]][1]  
    
        
    surface = 0
    perimeter = 0
    y = position[0]

    while position != start or perimeter == 0:

        (i, j) = position
        newDirection = findNextDirection(pipes, position, direction)        
        perimeter += 1
        
        if newDirection in [0, 2] and direction == 1:
            if newDirection == 0:
                y = i
            else:
                y= i+1
            
        if newDirection in [0, 2] and direction == 3:
            if newDirection == 0:
                y = i
            else:
                y = i+1
            
        if newDirection == 1 and direction in [0, 2]:
            if direction == 0:
                surface += y
        if newDirection == 3 and direction in [0, 2]:
            if direction == 2:
                surface -= y
        if newDirection == 0:
            if direction != 1:
                surface += y 
        if newDirection == 2:
            if direction != 3:
                surface -= y
            
        
        position = directionToPosition(newDirection, (i, j))
        direction = newDirection
    
    print(perimeter)
    print(abs(surface))
    print(abs(surface) - perimeter)
        
     
        
    
    
                                   
                             
main()

