import random
import Equations as Eqs
import math

def main():
	
	def checkIfCorrect( answer, equation ):
		
		solution = round( equation.solve(), 3 )
		ans = round( answer, 3 )
		correct = False
		
		if isinstance( solution, float ) or isinstance( solution, int ):
			correct = ( solution == ans )
		else if isinstance( solution, list ):
			for k in equation.solve():
				if round( k, 3 ) == ans:
					correct = True
					break
		
		return correct
	
	
	

main()