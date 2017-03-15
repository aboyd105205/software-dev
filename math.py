import random
import Equations as eqs
import math

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
	return userInput
	
def chooseEquation():
	random.seed()
	eqsChosen = random.randint (1, 1)
	print (eqsChosen)
	if eqsChosen == 1:
		chosenEq = lineFunc
		lineFunc()
	
# f(x) = mx + b
def lineFunc():
	lineFunc = eqs.LinearEquationY ( 10, 1, 15 )
	print(lineFunc.toString())

chooseEquation()

# Check input against real answer
userInput = getInput()
check = checkIfCorrect(userInput, chosenEq)

if check:
	print ("Good job!")
else:
	print ("Sorry, that's the wrong answer.")

