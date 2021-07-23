print('WELCOME')

import random

def game():
    print('Enter your choice\n ')
    user=input("'r' for rock,'p' for paper,'s' for scissor\n")
    print('You choose:',user)
    computer=random.choice(['s','r','p'])
    print('Computer Choice:',computer)

    if user==computer:
        return 'its a tie'
    
    if win(user,computer):
        return 'Hurrah!!!\n You Won'
    
    else:
        return 'You Lost\n Better luck Next time'



def win(you,opponent):
    if (you=='r' and opponent=='s') or (you=='s' and opponent=='p') or (you=='p' and opponent=='r'):
        return True

print(game())


