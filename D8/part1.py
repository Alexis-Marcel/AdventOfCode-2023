def parser():
    with open('input.txt') as f:
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


def main():
    lines = parser()
    
    ses = parseSequence(lines.pop(0).strip())
    lines.pop(0)
    
    map = parseMap(lines)
    
    actualKey = 'AAA'
    steps = 0
    i = 0
    while actualKey != 'ZZZ':
        actualKey = map[actualKey][int(ses[i])]
        steps += 1
        if i == len(ses) - 1:
            i = 0
        else:
            i += 1
    print(steps)
        
        
        
    
    
                             
                             
main()

