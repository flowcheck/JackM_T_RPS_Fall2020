from gameComponents import gameVars

def winorlose(status):

	if status == "won":
		pre_message = "You have won!"
	else:
		pre_message = "You have lost!"

	print(pre_message + "Play again?")

	choice = input ("Y / N? ")

	if choice == "N" or choice == "n":
		print("You selected No, Bye Loser! :)")
		exit()

	elif choice == "Y" or choice == "y":

		gameVars.player_lives = 5
		gameVars.computer_lives = 5
		gameVars.player = False
	else:
		print("Make a choice - Y or N")
		choice = input("Y / N: ")