import sys
import time

def parser():
    with open('input2.txt') as f:
        lines = f.readlines()
    return lines

#[79 14 55 13]
def parseSeedInterval(seedInfo):
    seeds = seedInfo.split(':')[1].split()
    intervals = []
    for i in range(0, len(seeds), 2):
        intervals.append((int(seeds[i]), int(seeds[i+1])))
    return intervals

def parseSeedMap(seedMap):
    
    map = []
    for line in seedMap:
        map.append(line.split())
    return map
    
def convertSeedsToLocation(seedsInterval, listMap):
    for i in range(len(listMap)):
        seedsInterval = matchInterval(seedsInterval, listMap[i])
    return seedsInterval
        

def matchInterval(seedsInterval, map):
    newSeedsInterval = []
    queue = seedsInterval

    for mapInterval in map:
        destination = int(mapInterval[0])
        sourceMap = int(mapInterval[1])
        rangeMap = int(mapInterval[2])
        mapBornInf = sourceMap
        mapBornSup = sourceMap + rangeMap
        tempQueue = []

        while queue:
            sourceSeed, rangeSeed = queue.pop(0)
            seedBornInf = sourceSeed
            seedBornSup = sourceSeed + rangeSeed

            # Cas où la seed est entièrement hors de l'intervalle de la carte
            if seedBornSup <= mapBornInf or seedBornInf >= mapBornSup:
                tempQueue.append((sourceSeed, rangeSeed))

            # Cas où la seed englobe l'intervalle de la carte
            elif seedBornInf <= mapBornInf and seedBornSup >= mapBornSup:
                if seedBornInf < mapBornInf:
                    tempQueue.append((sourceSeed, mapBornInf - sourceSeed))
                newSeedsInterval.append((destination, rangeMap))
                if seedBornSup > mapBornSup:
                    tempQueue.append((mapBornSup, seedBornSup - mapBornSup))

            # Cas où la seed est partiellement dans l'intervalle de la carte
            else:
                # Cas où le début de la seed est avant la carte
                if seedBornInf < mapBornInf:
                    tempQueue.append((sourceSeed, mapBornInf - sourceSeed))
                    overlap = min(seedBornSup, mapBornSup) - mapBornInf
                    newSeedsInterval.append((destination, overlap))
                # Cas où le début de la seed est dans la carte
                else:
                    overlap = min(seedBornSup, mapBornSup) - seedBornInf
                    newDestination = destination + seedBornInf - mapBornInf
                    newSeedsInterval.append((newDestination, overlap))
                    if seedBornSup > mapBornSup:
                        tempQueue.append((mapBornSup, seedBornSup - mapBornSup))

        queue = tempQueue

    for interval in queue:
        newSeedsInterval.append(interval)

    return newSeedsInterval


def main():
    timeStart = time.time()
    almanac = parser()
    
    seedsInterval = parseSeedInterval(almanac.pop(0))
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
        
    seedsInterval = convertSeedsToLocation(seedsInterval, listMap)
        
    lowest = sys.maxsize
    
    for (seed, range) in seedsInterval:
        lowest = min(lowest, seed)
    
    print(lowest)
    
    timeEnd = time.time()
    
    print("Time: " + str(timeEnd - timeStart))
            
                                    
main()

