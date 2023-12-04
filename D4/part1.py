def parser():
    with open('input.txt') as f:
        lines = f.readlines()
    return lines

#Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
def parseCard(card):
    
    numbers = card.split(':')[1]
    
    (winning, player) = numbers.split('|')
    
    winning = winning.split()
    player = player.split()
    
    return (winning, player)

def matchNumber(number, player):
    count = 0
    for i in range(len(player)):
        for j in range(len(number)):
            if player[i] == number[j]:
                count += 1
    return count

def main():
    cards = parser()
    
    sum = 0
    
    for card in cards:
        (winning, player) = parseCard(card)
        count = matchNumber(winning, player)
        if count != 0:
            sum += 2**(count-1)
        
    print(sum)               
                                    
main()

