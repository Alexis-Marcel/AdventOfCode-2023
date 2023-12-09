def parser():
    with open('input.txt') as f:
        lines = f.readlines()
    return lines

#0 1 2 3 
def parseData(lines):
    data = []
    for line in lines:
        line = list(map(int, line.split()))
        data.append(line)
    return data

def allZero(values):
    for value in values:
        if value != 0:
            return False
    return True

def extrapolate(values):
    
    findValue = 0
    
    while not allZero(values):
        temp = []
        findValue += values[-1]
        for i in range(len(values) - 1):
            temp.append(values[i + 1] - values[i])
        values = temp
    
    return findValue
    

def main():
    lines = parser()
    
    data = parseData(lines)
    
    sum = 0
    for values in data:
        sum += extrapolate(values)
    print(sum)
                                   
                             
main()

