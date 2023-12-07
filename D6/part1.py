def parser():
    with open('input.txt') as f:
        lines = f.readlines()
    return lines

#Time:      7  15   30
#Distance:  9  40  200
def parseRaces(lines):
    
    races = []
    
    times = lines[0].split(':')[1].split()
    distances = lines[1].split(':')[1].split()
    
    for i in range(len(times)):
        races.append((int(times[i]), int(distances[i])))
    
    return races
             
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
    
    races = parseRaces(lines)
    
    nbWay = 1
    
    for race in races:
        count = getNbWinningRace(race)
        nbWay *= count
    print(nbWay)
                                    
main()

