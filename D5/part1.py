def parser():
    with open('input.txt') as f:
        lines = f.readlines()
    return lines

def parseSeedMap(seedMap):
    
    map = []
    for line in seedMap:
        map.append(line.split())
    return map
    
def convertSeedToLocation(seed, listMap):
    for i in range(len(listMap)):
        seed = convertNumberMapped(seed, listMap[i])
    return seed
        

def convertNumberMapped(number, map):
    for i in range(len(map)):
        source = int(map[i][1])
        rangeMap = int(map[i][2])
        if source <= number:
            diff = number - source
            if diff < rangeMap:
                return int(map[i][0]) + diff
    return number

def main():
    almanac = parser()
    
    seeds = almanac.pop(0).split(':')[1].split()
    almanac.pop(0)
    almanac.pop(0)
    
    listMap = []
    
    currentMap = []
    for line in almanac:
        if line == '\n':
            listMap.append(parseSeedMap(currentMap))
            currentMap = []
            almanac.pop(0)
        else:
            currentMap.append(line)
    listMap.append(parseSeedMap(currentMap))
        
    lowest = convertSeedToLocation(int(seeds[0]), listMap)
    seeds.pop(0)
    for seed in seeds:
        lowest = min(lowest, convertSeedToLocation(int(seed), listMap))
        
        
    print(lowest)
            
                                    
main()

