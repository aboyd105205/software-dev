import sys
import random
import Equations as eqs
import math

def main():

	# Section for equation functions
	
	# f(x) = mx + b, solve for f(x)
	def lineFuncY(num1, num2, num3):
		lineFuncY = eqs.LinearEquationY(num1, num2, num3)
		print(lineFuncY.toString())
		return lineFuncY
	#f(x) = mx + b, solve for x
	def lineFuncX(num1, num2, num3):
		lineFuncX = eqs.LinearEquationX(num1, num2, num3)
		print(lineFuncX.toString())
		return lineFuncX
		
		
		
	# Computing section
	def checkIfCorrect( answer, equation ):
		
		solution = round( equation.solve(), 3 )
		ans = round( answer, 3 )
		correct = False
		
		if isinstance( solution, float ) or isinstance( solution, int ):
			correct = ( solution == ans )
		elif isinstance( solution, list ):
			for k in equation.solve():
				if round( k, 3 ) == ans:
					correct = True
					break
		
		return correct

	def getInput():
		userInput = input('Please enter the correct answer for the unknown variable: ')
		
		if userInput == "quit":
			sys.exit()
		
		while True:
			try:
				userInput = float(userInput)
				break
			except ValueError:
				userInput = input ("Please input an actual number: ")
		return userInput
		
	def chooseEquation():
		random.seed()
		eqsChosen = random.randint (1, 2)
		randNum1 = random.randint (-20, 20)
		randNum2 = random.randint (-20, 20)
		randNum3 = random.randint (-20, 20)
		
		while randNum1 == 0:
			randNum1 = random.randint(-20, 20)
		
		if eqsChosen == 1:
			chosenEq = lineFuncY(randNum1, randNum2, randNum3)
			return chosenEq
		elif eqsChosen == 2:
			chosenEq = lineFuncX(randNum1, randNum2, randNum3)
			return chosenEq

	chosenEq = chooseEquation()

	# Check input against real answer
	userInput = getInput()	
	check = checkIfCorrect(userInput, chosenEq)
	correct = round( chosenEq.solve(), 3 )

	if check:
		print ("Good job!")
	else:
		print ("Sorry, that's the wrong answer. It was actually {0}.".format (correct))

while True:
	main()
