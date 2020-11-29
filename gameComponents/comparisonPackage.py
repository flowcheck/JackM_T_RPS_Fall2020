from random import randint

from gameComponents import gameVars


computer = gameVars.choices[randint(0, 2)]

def comparison(status):

		if (computer == gameVars.player):
			print("tie")

		elif (computer == "rock"):
			if (gameVars.player == "paper"):
				gameVars.player_lives -= 1
				print("you lose! sucker! player lives: ", gameVars.player_lives)
			else:
				print("you win! winner!")
				gameVars.computer_lives -= 1

		elif (computer == "paper"):
			if (gameVars.player== "scissors"):
				gameVars.player_lives -= 1
				print("you lose! sucks to be you! player lives: ", gameVars.player_lives)
			else:
				print("you win! you pro you!")
				gameVars.computer_lives -=1

		elif (computer == "scissors"):
			if (gameVars.player == "rock"):
				gameVars.player_lives -= 1
				print("you lose! lol loser! player lives: ", gameVars.player_lives)
			else:
				print("you win! congrats!")
				gameVars.computer_lives -= 1