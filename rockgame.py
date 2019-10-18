#import the random module
import random
#Sets winner variable to a string
winner = ''
wins = 0
losses = 0
choices = ['rock', 'paper', 'scissors']

print("Rock, Paper Scissors! First to 5 wins")

#Makes the computer choose a random option
while wins < 5 and losses < 5:
	computer_choice = random.choice(choices)
	#asks the user for an option if invalid reprompts
	user_choice = ''
	while (user_choice not in choices):
		user_choice = input('rock, paper, or scissors? ')
	#Decides who wins
	if user_choice == computer_choice:
		winner = 'Tie'
	elif computer_choice == 'rock' and user_choice == 'scissors':
		winner = 'Computer'
	elif computer_choice == 'paper' and user_choice == 'rock':
		winner = 'Computer'
	elif computer_choice == 'scissors' and user_choice == 'paper':
		winner = 'Computer'
	else:
		winner = 'User'
	#print out the results
	if winner == 'Tie':
		print('It was a tie, no one won.')
	elif winner == 'User':
		wins += 1
		print("Player won! ", 'The user chose ', user_choice, ". The computer chose ", computer_choice, ".")
		print("Wins:", wins)
		print("Losses:", losses)
	else:
		losses += 1
		print(winner, ' won! ', 'The computer chose ', computer_choice, '.', ' The user chose ', user_choice, '. Try again next time!')
		print("Wins:", wins)
		print("Losses:", losses)
if wins == 5:
	print("Congratulations!!! You bested the computer")
else:
	print("Aww the computer won this time, try again for another chance to win")
