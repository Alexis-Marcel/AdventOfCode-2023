def parser():
    with open('input.txt') as f:
        lines = f.readlines()
    return lines

def findFirstDigit(str) :
    for i in range(len(str)):
        if str[i].isdigit():
            return str[i]
    return -1

def findEndDigit(str) :
    for i in range(len(str)-1, -1, -1):
        if str[i].isdigit():
            return str[i]
    return -1


def main() :
    
    lines = parser()
    
    acc = []
    
    for line in lines:
        acc.append(int(findFirstDigit(line) + findEndDigit(line)))
        
    res = sum(acc)
    print(res)
    
    
    
    
    
main()
