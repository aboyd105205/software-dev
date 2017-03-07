import random
import Equations

def main():
	
	def checkIfCorrect( answer, equation ):
		correct = False
		for i, k in equation.solve():
			if k == answer:
				correct = True
				break
		return correct
	
	
	

main()