import random
comp= random.randint(0,2)

#print('2->Gun\n 1->Snake\n 3->Water')
user = int(input(' 2->Gun\n 1->Snake\n 0->Water\n'))

def checkWinner(comp,user):
    if comp==user:
        print(f'Computer chose {comp} and You chose {user}')
        return 'DRAW'
    elif (user==1 and comp==2) or (user==0 and comp==1) or (user==2 and comp==0):
        print(f'Computer chose {comp} and You chose {user}')
        return 'You Lose'
    else:
        print(f'Computer chose {comp} and You chose {user}')
        return 'You Win'

result=checkWinner(comp,user)
print(result)