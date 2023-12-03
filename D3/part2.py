def parser():
    with open('input2.txt') as f:
        lines = f.readlines()
    return lines

def checkPartNumber(engine, i, j, length):
    
    if i+1 < len(engine[j])-1:
        if not engine[j][i+1].isdigit() and not engine[j][i+1] == '.':
            return (j, i+1)
        borneSup = i+1
    else:
        borneSup = i
    
    if i - length >= 0:
        if not engine[j][i-length].isdigit() and not engine[j][i-length] == '.':
            return (j, i-length)
        borneInf = i - length
    else: 
        borneInf = 0
            
    if j + 1 < len(engine)-1:
        for k in range(borneInf, borneSup+1):
            if not engine[j+1][k].isdigit() and not engine[j+1][k] == '.':
                return (j+1, k)
    
    if j - 1 >= 0:
        for k in range(borneInf, borneSup+1):
            if not engine[j-1][k].isdigit() and not engine[j-1][k] == '.':
                return (j-1, k)
    
    return -1

def main():
    engine = parser()
    
    gear = {}
    
    sum = 0
    
    for j in range(len(engine)):
        i = 0
        while i < len(engine[j]):
            if engine[j][i].isdigit():
                number = engine[j][i]
                while i+1 < len(engine[j]) and engine[j][i+1].isdigit():
                    number += engine[j][i+1]
                    i += 1
                res= checkPartNumber(engine, i, j, len(number)) 
                if res != -1:       
                    if engine[res[0]][res[1]] == '*':
                        gear.setdefault((res[0], res[1]), []).append(int(number))
                i += 1
            else :
                i += 1
    for key in gear:
        if len(gear[key]) == 2:
            sum += gear[key][0] * gear[key][1]
    print(sum)
                
                                    
main()

