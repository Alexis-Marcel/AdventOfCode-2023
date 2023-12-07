def parser():
    with open('input2.txt') as f:
        lines = f.readlines()
    return lines

#Time:      7  15   30
#Distance:  9  40  200
def parseRace(lines):
    timeInfo = lines[0]
    distanceInfo = lines[1]
    
    races = []
    
    time = timeInfo.split(':')[1].replace(' ', '')
    distance = str(distanceInfo.split(':')[1].replace(' ', ''))

    return (int(time), int(distance))
             
def getNbWinningRace(race):
    count = 0
    (time, distance) = race
    
    for i in range(1,time+1):
        timeLeft = time - i
        newDistance = timeLeft * i
        
        if newDistance > distance:
            count += 1
    return count
        
        
         

def main():
    lines = parser()
    
    race = parseRace(lines)
    
    print(getNbWinningRace(race))

                                    
main()

