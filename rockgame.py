#import the random module
import random
#Sets winner variable to a string
winner = ''
wins = 0
losses = 0
print("Rock, Paper Scissors! First to 5 wins")

#Makes the computer choose a random option
while wins < 5 and losses < 5:
	random_choice = random.randint(0,2)
	if random_choice == 0:
		computer_choice = 'rock'
	elif random_choice == 1:
		computer_choice = 'paper'
	else:
		computer_choice = 'scissors'
	#asks the user for an option if invalid reprompts
	user_choice = ''
	while (user_choice != 'rock' and
		user_choice != 'paper' and
		user_choice != 'scissors'):
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

