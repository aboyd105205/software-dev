import random

def main():
	numOne = random.randint (0, 1)
	numTwo = random.randint (0, 1)
	
	# Define variables and calculate for the unknown
	if numOne == 0:
		x = random.randint (1, 20)
	else:
		x = random.randint (-20, -1)

	if numTwo == 0:
		y = random.randint (1, 20)
	else:
		y = random.randint (-20, -1)
		
	unknown = random.randint (-20, 20)
	if unknown == 0:
	  unknown = unknown + 1
	
	answer = (x * unknown) + y
	
	# Display finished equation for solving
	print (str(x) + " * " + ' X ' + " + " + str(y) + " = " + str(answer))
	
	answer_x = input("What is X? ")
	
	# Check input against answer and respond
	if int(answer_x) == unknown:
	  print ("Good job!")
	else:
		print ("Sorry, the answer is " + str(unknown))
	
main()
