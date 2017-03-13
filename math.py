import random
import Equations as eqs


def getInput():
	userInput = input('Please enter the correct answer for the unknown variable: ')
	return int(userInput)
	
def checkIfCorrect( answer, equation ):
	return answer == equation.solve()
	
# f(x) = mx + b
lineFunc = eqs.LinearEquationY ( 10, 1, 15 )
print(lineFunc.toString())

# Check input against real answer
userInput = getInput()
check = checkIfCorrect(userInput, lineFunc)

if check == True:
	print ("Good job!")
else:
	print ("Sorry, that's the wrong answer.")

