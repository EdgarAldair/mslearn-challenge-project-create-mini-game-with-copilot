# write 'hello world' to the console
print('hello world')
#want a rock siccors paper game, first of all, we need to import random, the player can choose first
#then the computer will choose randomly, then we need to compare the result, then we need to print the result
#The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
#At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
#By the end of each round, the player can choose whether to play again.
#Display the player's score at the end of the game.
#The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

import random
print('Welcome to the rock paper scissors game')
print('Please enter your choice')
player_choice = input('rock, paper, or scissors? ')
player_choice = player_choice.lower()
print('You chose', player_choice)
computer_choice = random.choice(['rock', 'paper', 'scissors'])
print('The computer chose', computer_choice)
if player_choice == computer_choice:
    print('You tied!')
elif player_choice == 'rock' and computer_choice == 'scissors':
    print('You win!')
elif player_choice == 'paper' and computer_choice == 'rock':
    print('You win!')
elif player_choice == 'scissors' and computer_choice == 'paper':
    print('You win!')
else:
    print('You lose!')
    


