#------------------------------------------------------------------------------
# Chloe Jiang
# cfjiang@ucsc.edu
# programming assignment 3
# This program plays a guessing game with the user.
#------------------------------------------------------------------------------
import random

print("I'm thinking of an integer in the range 1 to 10. You have three guesses \n")
number = random.randint(1, 10)
guess1 = int(input("Enter your first guess: "))
if guess1 < number:
	print("Your guess is too low. \n")
	
	guess2 = int(input("Enter your second guess: "))
	if guess2< number:
		print("Your guess is too low \n")
		
		guess3 = int(input("Enter your third guess: "))
		if guess3< number:
			print("Your guess is too low \n")
			print("You lose. The number was " +str(number)+".")
		elif guess3 > number:
			print("Your guess is too high \n")
			print("You lose. The number was " +str(number)+".")
		else:
			print("You win!")

	elif guess2 > number:
		print("Your guess is too high \n")

		guess3 = int(input("Enter your third guess: "))
		if guess3< number:
			print("Your guess is too low \n")
			print("You lose. The number was " +str(number)+".")
		elif guess3 > number:
			print("Your guess is too high \n")
			print("You lose. The number was " +(number)+".")
		else:
			print("You win!")
			

	else:
		print("You win!")
		

if guess1 > number:
	print("Your guess is too high. \n")
	
	guess2 = int(input("Enter your second guess: "))
	if guess2< number:
		print("Your guess is too low \n")
		
		guess3 = int(input("Enter your third guess: "))
		if guess3< number:
			print("Your guess is too low \n")
			print("You lose. The number was " +str(number)+".")
		elif guess3 > number:
			print("Your guess is too high \n")
			print("You lose. The number was " +str(number)+".")
		else:
			print("You win!")
			

	elif guess2 > number:
		print("Your guess is too high \n")

		guess3 = int(input("Enter your third guess: "))
		if guess3< number:
			print("Your guess is too low \n")
			print("You lose. The number was " +str(number)+".")
		elif guess3 > number:
			print("Your guess is too high \n")
			print("You lose. The number was " +str(number)+".")
		else:
			print("You win!")
			
			
	else:
		print("You win!")
		

