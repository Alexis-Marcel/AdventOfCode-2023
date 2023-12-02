def parser():
    with open('input2.txt') as f:
        lines = f.readlines()
    return lines

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
def parseGameInformation(game):
    
    (gameInfo, bag) = game.split(':')
    
    gameId = int(gameInfo.split()[1])
    
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

def getGamePower(sets):
    power = 0
    maxRed, maxGreen, maxBlue = 0, 0, 0
    for set in sets:
        maxRed = max(maxRed, set[0])
        maxGreen = max(maxGreen, set[1])
        maxBlue = max(maxBlue, set[2])
    return maxRed * maxGreen * maxBlue
              
def main() :
    
    lines = parser()
    
    sumPower = 0
    
    for line in lines:
        (gameId, sets) = parseGameInformation(line)
        sumPower += getGamePower(sets)
    print(sumPower)
    
    
main()
