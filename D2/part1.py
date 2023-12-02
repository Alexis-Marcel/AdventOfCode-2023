def parser():
    with open('input.txt') as f:
        lines = f.readlines()
    return lines

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
def parseGameInformation(line):
    
    (game, bag) = line.split(':')
    
    gameId = int(game.split()[1])
    
    strSets = bag.split(';')
    
    sets = []
    for i in range(len(strSets)):
        set = [0, 0, 0]
        strSet = strSets[i].split(',')
        for j in range(len(strSet)):
            (num, color) = strSet[j].split()
            if color == 'red':
                set[0] += int(num)
            elif color == 'green':
                set[1] += int(num)
            elif color == 'blue':
                set[2] += int(num)
        sets.append(set)
        
    return (gameId, sets)

def gameIsValid(sets, gameId):
    maxBag = [12, 13, 14]

    for i in range(len(sets)):
        for j in range(len(sets[i])):
            if sets[i][j] > maxBag[j]:
                return False
    return True
              
def main() :
    
    lines = parser()
    
    sumId = 0
    
    for line in lines:
        (gameId, sets) = parseGameInformation(line)
        if gameIsValid(sets, gameId):
            sumId += gameId
    print(sumId)
            
    
    
    
    
    
    
main()
