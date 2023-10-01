# rock, paper, scissor
# module 
import random

actions=['paper','scissor','rock']
computer_choice=random.choice(actions)


user_choice=input("enter your choice 'rock' or 'paper' or 'scissor' ")

if computer_choice==user_choice:
    print('both choosed same no one win game tie ')


elif computer_choice=='rock':
    if user_choice=='scissor':
        print('rock smash scissor you lose')
    else:
        print('paper smash rock you win')


elif computer_choice=='paper':
    if user_choice=='rock':
        print('paper smash rock you lose')
    else:
        print('scissor cut paper you win')


elif computer_choice=='scissor':
    if user_choice=='rock':
        print('rock smash scissor you win')
    else: 
        print('you lose')


print(f"your choice is {user_choice} and computer choice is {computer_choice}")
