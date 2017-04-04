import sys
import random
import Equations as eqs
import math
import tkinter as tk
import tkinter.messagebox as msgs
random.seed()

def main():
	
	# UI
	
	#Make the frame
	class UserInterface(tk.Frame):
		def __init__(self, master=None):
			super().__init__(master)
			self.pack()
			self.create_widgets()
			self.buttonlistener = 0
			self.minsize( 512,512 )
		
		def incrementButton():
			self.buttonlistener = self.buttonlistener + 1
		
		def create_widgets(self):
			
			self.EntryBox = tk.Entry( self )
			self.EntryBox.pack( side = "bottom" )
			self.EntryBox["geometry"] = "128x32"
			
			self.Enter = tk.Button( self, text = "enter" )
			self.Enter.command = self.incrementButton
			self.Enter.pack( side = "right" )
			self.Enter["geometry"] = "32x32"
			
			self.TextDisplay = tk.Label( self, text="---------------" )
			self.TextDisplay.pack()
			self.TextDisplay["geometry"] = "160x32"
			
		def SetDisplay( str ):
			self.TextDisplay.text = str
		
		def GetButtonValue():
			return self.buttonlistener
		
		def GetInput():
			return self.EntryBox.get()
		
	def Msg( str ):
		msgs.showinfo( "", str )
	
	# Section for equation functions
	
	# f(x) = mx + b, solve for f(x)
	def lineFuncY(num1, num2, num3):
		lineFuncY = eqs.LinearEquationY(num1, num2, num3)
		return lineFuncY
	#f(x) = mx + b, solve for x
	def lineFuncX(num1, num2, num3):
		lineFuncX = eqs.LinearEquationX(num1, num2, num3)
		return lineFuncX
	#f(x) = mx^2 + b, solve for y
	def quadFuncY(num1, num2, num3):
		quadFuncY = eqs.QuadraticEquationY(num1, num2, num3)
		return quadFuncY
	#f(x) = mx^2 + b, solve for x
	def quadFuncX(num1, num2, num3):
		quadFuncX = eqs.QuadraticEquationX(num1, num2, num3)
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
		
		while True:
			try:
				userInput = float(eval(userInput))
				break
			except (NameError,SyntaxError,ValueError):
				userInput = input ("Please input an actual number: ")
		return userInput
	
	def rand():
		rando = random.randint (-20, 20)
		while rando == 0:
			rando = random.randint (-20, 20)
		return rando
	
	def sign(n):
		sign = 0
		if n > 0:
			sign = 1
		elif n < 0:
			sign = -1
		return sign
	
	def listToString( l ):
		length = len(l)
		string = ""
		for i in range(length-1):
			string = string + str(l[i]) + ", "
		string = string + "or " + str(l[length-1])
		return string
	
	def chooseEquation():
		eqsChosen = random.randint (1, 4)
		
		if eqsChosen == 1:
			chosenEq = lineFuncY(rand(), rand(), rand())
			return chosenEq
		elif eqsChosen == 2:
			chosenEq = lineFuncX(rand(), rand(), rand())
			return chosenEq
		elif eqsChosen == 3:
			chosenEq = quadFuncY(rand(), rand(), rand())
			return chosenEq
		elif eqsChosen == 4:
			chosenEq = quadFuncX(rand(), rand(), rand())
			return chosenEq
	
	# Actual user interaction
	state = "setupEq"
	
	Msg("\nYou will be given a random mix of linear and quadratic equations in which some will have you solve for X, and others for Y.")
	
	userInput = ""
	
	ui = UserInterface(tk.Tk())
	ui.mainloop()
	
	chosenEq = False
	buttonValue = False
	
	
	while True:
		
		if state=="setupEq":
			
			chosenEq = chooseEquation()
			userInput = getInput()
			
			ui.SetDisplay( chosenEq.toString() )
		
		elif state=="input":
			
			if buttonValue != ui.GetButtonValue():
				buttonValue = ui.GetButtonValue()
				userInput = ui.GetInput()
				state = "check"
		
		elif state=="check":
			
			check = checkIfCorrect( float(eval(userInput)), chosenEq )
			
			if check:
				Msg("Good job!")
				state = "setupEq"
			else:
				if  isinstance(correct,float) or isinstance(correct,int):
					Msg("Sorry, that's the wrong answer. It was actually {0}.".format(correct))
				elif isinstance(correct,list):
					Msg("Sorry, that's the wrong answer. It was actually {0}.".format(listToString(correct)))	
main()