
kolor = ['Kier','Karo','Pik','Trefl']
figura = [{'figura':'As','Siła':14},
          {'figura':'Król','Siła':13},
          {'figura':'Dama','Siła':12},
          {'figura':'Jopek','Siła':11},
          {'figura':'10','Siła':10},
          {'figura':'9','Siła':9}]

allCards = []

for k in kolor:
    for f in figura:
        aCard = f.copy()
        aCard['Kolor'] = k
        allCards.append(aCard)

import random
random.shuffle(allCards)

player1 = allCards[:12]
player2 = allCards[12:]

print('Karty pierwszego gracza: \n',player1)
print('\nKarty drugiego gracza: \n',player2)

while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    stack = []

    if card1['Siła'] == card2['Siła']:
        while card1['Siła'] == card2['Siła']:
            print('WOJNA \t %d \t %d \t' % (card1["Siła"], card2["Siła"]))
            stack.append(card1)
            stack.append(card2)

            if len(player1) < 2:
                player2.extend(stack)
                player2.extend(player1)
                player1 = []
                print('PLAY-2 \t %d \t %d \t' % (card1["Siła"], card2["Siła"]) + len(player2)*'*')
                break
            
            elif len(player2) < 2:
                player1.extend(stack)
                player1.extend(player1)
                player2 = []
                print('PLAY-1 \t %d \t %d \t' % (card1["Siła"], card2["Siła"]) + len(player1)*'*')
                break
            
            else:
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                stack.append(card1)
                stack.append(card2)
                card1 = player1.pop(0)
                card2 = player2.pop(0)
        else:
            if card1['Siła'] > card2['Siła']:
                stack.append(card1)
                stack.append(card2)
                player1.extend(stack)
                print('PLAY-1 \t %d \t %d \t' % (card1["Siła"], card2["Siła"]) + len(player1)*'*')
            else:
                stack.append(card1)
                stack.append(card2)
                player2.extend(stack)
                print('PLAY-2 \t %d \t %d \t' % (card1["Siła"], card2["Siła"]) + len(player2)*'*')
            
    elif card1['Siła'] > card2['Siła']:
        player1.append(card1)
        player1.append(card2)
        print('PLAY-1 \t %d \t %d \t' % (card1["Siła"], card2["Siła"]) + len(player1)*'*')

    else:
        player2.append(card1)
        player2.append(card2)
        print('PLAY-2 \t %d \t %d \t' % (card1["Siła"], card2["Siła"]) + len(player2)*'*')

if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    print('PLAYER 2 WON!!!!')
