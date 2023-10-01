import random
actions = [ 'paper' , 'scissor' , 'rock' ]

computer=random.choice(actions)

user=input("Enter your choice 'rock' or 'paper' or 'scissor'\n")
if user == computer:
    print('Both are Same Match Draw')

elif user=='paper':
    if computer=='rock':
        print('you win ')
    elif computer=='scissor':
        print('you lose')

elif user=='rock':
    if computer=='paper':
        print('you lose')
    elif computer=='scissor':
        print('You win')

elif user=='scissor':
    if computer=='paper':
        print('you win')
    elif computer=='rock':
        print('you lose')

print(f"computer choosed {computer} and you choosed {user  }")