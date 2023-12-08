import math

def parser():
    with open('input2.txt') as f:
        lines = f.readlines()
    return lines

#LLR
def parseSequence(sequence):
    sequence = sequence.replace('L', '0')
    sequence = sequence.replace('R', '1')
    return sequence    

#AAA = (BBB, BBB)
def parseMap(lines):
    map = {}
    for line in lines:
        line = line.strip()
        (key, value) = line.split(' = ')
        #enlever les parenthèses
        keyValue = value[1:-1].split(', ')
        map[key] = keyValue
    return map

def findStartKeys(map):
    keys = []
    for key in map.keys():
        if key[-1] == 'A':
            keys.append(key)
    return keys

def isFinishKeys(keys):
    for key in keys:
        if key[-1] != 'Z':
            return False
    return True

def main():
    lines = parser()
    
    ses = parseSequence(lines.pop(0).strip())
    lines.pop(0)
    
    map = parseMap(lines)
    
    keys = findStartKeys(map)
    
        
    i = 0
    steps = []
    for key in keys:
        count = 0
        while key[-1] != 'Z':
            key = map[key][int(ses[i])]
            count += 1
            if i == len(ses) - 1:
                i = 0
            else:
                i += 1
        steps.append(count)
    
    res = math.lcm(*steps)
    
    print(res)                     
                             
main()

