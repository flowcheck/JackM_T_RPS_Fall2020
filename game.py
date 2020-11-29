from random import randint

from gameComponents import gameVars, winLose, comparisonPackage

while gameVars.player == False:
	print("================*/ RPS GAME */================")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("==============================================")
	print("Make your choice! or type quit to exit\n")

	gameVars.player = input("Choose rock, paper or scissors: \n")

	if gameVars.player == "quit":
		print("you chose to quit")
		exit()

	computer = gameVars.choices[randint(0, 2)]

	print("user chose: " + gameVars.player)

	print("AI chose: " + computer)

	comparisonPackage.comparison(gameVars.player)

	if gameVars.player_lives == 0:
		winLose.winorlose("lost")

	elif gameVars.computer_lives == 0:
		winLose.winorlose("won")

	else:
		gameVars.player = False

	print("player lives:", gameVars.player_lives, "lives left")
	print("computer lives", gameVars.computer_lives, "lives left")