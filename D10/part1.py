def parser():
    with open('input.txt') as f:
        lines = f.readlines()
    return lines

#0 : droite, 1 : bas, 2 : gauche, 3 : haut
pipesMapConvert = { '-' : (0, 2), '|' : (1, 3), 'L' : (2, 1), 'F' : (3, 2), 'J' : (0, 1), '7' : (0, 3), '.' : (-1, -1), 'S' : 'S'}

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
            temp.append(pipesMapConvert[line[j]])
        pipes.append(temp)
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

def findStartDirection(pipes, start):
    (i, j) = start
    n = len(pipes)
    
    for k in range(4):
        if k == 0 and j + 1 < n and (pipes[i][j + 1][0] == k or pipes[i][j + 1][1] == k):
            return (i, j + 1), k
        
        if k == 1 and i + 1 < n and (pipes[i + 1][j][0] == k or pipes[i + 1][j][1] == k):
            return (i + 1, j), k
        if k == 2 and j - 1 >= 0 and (pipes[i][j - 1][0] == k or pipes[i][j - 1][1] == k):
            return (i, j - 1), k
        if k == 3 and i - 1 >= 0 and (pipes[i - 1][j][0] == k or pipes[i - 1][j][1] == k):
            return (i - 1, j), k
    return (-1, -1), -1
        
def main():
    lines = parser()
    
    (pipes, start) = parsePipes(lines)
    
    (position, direction) = findStartDirection(pipes, start)
    
    perimeter = 0
    while position != (-1, -1):
        (i, j) = position
        if pipes[i][j][0] == direction:
            newDirection = invertDirection(pipes[i][j][1])
        else:
            newDirection = invertDirection(pipes[i][j][0])

        position = directionToPosition(newDirection, (i, j))
        direction = newDirection
        perimeter += 1
    print(perimeter//2)
        
    
        
    
    
                                   
                             
main()

