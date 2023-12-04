def parser():
    with open('input2.txt') as f:
        lines = f.readlines()
    return lines

#Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
def parseCard(card):
    
    (cardInfo, numbers) = card.split(':')
    
    id = int(cardInfo.split()[1])
    
    (winning, player) = numbers.split('|')
    
    winning = winning.split()
    player = player.split()
    
    return (id, winning, player)

def matchNumber(number, player):
    count = 0
    for i in range(len(player)):
        for j in range(len(number)):
            if player[i] == number[j]:
                count += 1
    return count

def main():
    lines = parser()
        
    cards = []
    
    for line in lines:
        (id, winning, player) = parseCard(line)
        cards.append((id, matchNumber(winning, player)))        
    
    gameList = []
    
    for i in range(len(cards)-1, -1, -1):
        (id, count) = cards[i]
        nbCard =0
        for j in range(count):
            (id2, count2) = gameList[len(gameList)-1-j]
            nbCard += 1 + count2
        gameList.append((id, nbCard))
    
    sum = 0
    for (id, count) in gameList:
        sum += 1+count
        
    print(sum)
        
    
        
        
main()

