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
	#f(x) = mx^2 + b, solve for x
	def quadFuncX(num1, num2, num3):
		quadFuncX = eqs.QuadraticEquationX(num1, num2, num3)
		print(quadFuncX.toString())
		return quadFuncX
		
		
	# Computing section
	def checkIfCorrect( answer, equation ):
		
		solution = equation.solve()
		ans = round( answer, 3 )
		correct = False
		
		if isinstance( solution, float ) or isinstance( solution, int ):
			correct = ( round(solution,3) == ans )
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
				userInput = float(eval(userInput))
				break
			except (NameError,SyntaxError,ValueError):
				userInput = input ("Please input an actual number: ")
		return userInput
		
	def rand():
		random.seed()
		rando = random.randint (-20, 20)
		while rando == 0:
			rando = random.randint (-20, 20)
		return rando
	
	def sign(n):
		return int(n / abs(n))
	
	def listToString( l ):
		length = len(l)
		string = ""
		for i in range(length-1):
			string = string + str(l[i]) + ", "
		string = string + "or " + str(l[length-1])
		return string
		
	
	def chooseEquation():
		eqsChosen = random.randint (1, 3)
		num1 = rand()
		num2 = rand()
		num3 = rand()
		
		if eqsChosen == 1:
			chosenEq = lineFuncY(num1, num2, num3)
			return chosenEq
		elif eqsChosen == 2:
			chosenEq = lineFuncX(num1, num2, num3)
			return chosenEq
		elif eqsChosen == 3:
			chosenEq = quadFuncX(num1,num2,num3)
			return chosenEq

	chosenEq = chooseEquation()

	# Check input against real answer
	userInput = getInput()	
	check = checkIfCorrect(userInput, chosenEq)
	correct = chosenEq.solve()

	if check:
		print ("Good job!")
	else:
		if  isinstance(correct,float) or isinstance(correct,int):
			print ("Sorry, that's the wrong answer. It was actually {0}.".format (correct))
		elif isinstance(correct,list):
			print ("Sorry, that's the wrong answer. It was actually {0}.".format (listToString(correct)))	

while True:
	main()
