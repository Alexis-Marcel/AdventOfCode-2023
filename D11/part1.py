import math

def parser():
    with open('input.txt') as f:
        lines = f.readlines()
    return lines

def parseGalaxy(lines):
    noGalaxyLines = [ True for i in range(len(lines))]
    noGalaxyColumns = [ True for i in range(len(lines[0])-1)]
    galaxy = []
    
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            if line[j] == '#':
                galaxy.append((i, j))
                noGalaxyLines[i] = False
                noGalaxyColumns[j] = False
    return galaxy, noGalaxyLines, noGalaxyColumns
        
def main():
    lines = parser()
    
    galaxy, noGalaxyLines, noGalaxyColumns = parseGalaxy(lines)
    
    countSteps = []
    n = len(galaxy)
    for i in range(n):
        for j in range(i+1, n):
            (x1, y1) = galaxy[i]
            (x2, y2) = galaxy[j]

            xSteps = abs(x1 - x2)
            ySteps = abs(y1 - y2) 
                
            count = xSteps + ySteps
                
            for k in range(min(x1, x2)+1, max(x1, x2)):
                if noGalaxyLines[k]:
                    count += 1
            for k in range(min(y1, y2)+1, max(y1, y2)):
                if noGalaxyColumns[k]:
                    count += 1
            countSteps.append(count)
    print(sum(countSteps))
                
            
    
                             
main()

