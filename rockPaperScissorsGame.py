import random

# Rock✊, Paper✋, and Scissor✌ game
'''
Rule Book:
        ✊ > ✌
        ✋ > ✊
        ✌ > ✋
        or
        3 bit 2, 2 bit 1, 1 bit 3
'''


def choice(u_choice, c_choice):
    print('User choose: ', end='')
    if u_choice==1:
        print(rock)
    elif u_choice==2:
        print(paper)
    elif u_choice==3:
        print(scissor)
    else:
        print('Invalid input')

    
    print('Computer choose: ', end='')
    if c_choice==1:
        print(rock)
    elif c_choice==2:
        print(paper)
    else:
        print(scissor)


def conditionToWin(u_c, c_c):
    
    if u_c >=4 or u_c < 1:
        print('You typed an Invalid number, You lose!')
    elif u_c==1 and c_c==3:
        print('You win!')
    elif c_c==1 and u_c==3:
        print('You lose!')
    elif u_c == c_c:
        print("It's a draw!")
    elif c_c > u_c:
        print('You lose!')
    elif u_c > c_c:
        print('You Win!')
    

rock = '✊ 🗿'
paper = '✋ 📄'
scissor = '✌ ✂'

user_choice = int(input("What do you want to choose?. 1 For Rock, 2 For Paper or 3 For Scissors: "))
computer_choice = random.randint(1, 3)

choice(user_choice, computer_choice)

conditionToWin(user_choice, computer_choice)
