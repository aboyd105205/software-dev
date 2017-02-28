import random

def main():
	numOne = random.randint (0, 1)
	numTwo = random.randint (0, 1)
	
	if numOne == 0:
		x = random.randint (0, 20)
	else:
		x = random.randint (-20, 0)

	if numTwo == 0:
		y = random.randint (0, 20)
	else:
		y = random.randint (-20, 0)
		
	unknown = random.randint (0, 20)
	answer = (x * unknown) + y
	
	print (str(x) * 'X' + str(y) '=' str(answer))
	
main()
