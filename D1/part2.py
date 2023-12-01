convert = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
           'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def parser():
    with open('input2.txt') as f:
        lines = f.readlines()
    return lines

def convertToNum(string):
    for key in convert:
        if key in string:
            return convert[key]
    return -1

def findFirstDigit(string):
    buff = ''
    for i in range(len(string)):
        if string[i].isdigit():
            return string[i]
        else:
            buff += string[i]
            res = convertToNum(buff)
            if res != -1:
                return res
    return -1


def findEndDigit(string):
    buff = ''
    for i in range(len(string)-1, -1, -1):
        if string[i].isdigit():
            return string[i]
        else:
            buff = string[i] + buff
            res = convertToNum(buff)
            if res != -1:
                return res
    return -1


def main():

    lines = parser()

    acc = []

    for line in lines:
        first = findFirstDigit(line)
        end = findEndDigit(line)
        if first != -1 and end != -1:
            print((first, end))
            acc.append(int(first + end))

    res = sum(acc)
    print(res)


main()
