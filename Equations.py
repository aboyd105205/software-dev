from abc import ABCMeta, abstractmethod

class Equation:
	
	__metaclass__ = ABCMeta
	
	# abstract method that must be overridden for a class to work
	@abstractmethod
	def solve(self):
		pass
	
	@abstractmethod
	def toString(self):
		pass
	

# an equation of the type f(x) = mx + b
# this version solves for x
class LinearEquationX(Equation):
	
	def __init__( self, m, b, fx ):
		self.slope = m
		self.offset = b
		self.known = fx
	
	def solve(self):
		return ( ( self.known - self.offset ) / self.slope, )
	
	def toString(self):
		return '{0} = {1}*x + {2}'.format( *(self.known, self.slope, self.offset) )

# an equation of the type f(x) = mx + b
# this version solves for f(x)
class LinearEquationY(Equation):
	
	def __init__( self, m, b, x ):
		self.slope = m
		self.offset = b
		self.known = x
	
	def solve(self):
		return ( self.known * self.slope + self.offset, )
	
	def toString(self):
		return 'f(x) = {0}*{1} + {2}'.format( *(self.slope, self.known, self.offset) )

# class SineSolutionEquation(Equation):
	
	# def __init__( self, start, end, freqMult, offset ):
		# self.min = start
		# self.max = end
		# self.freqMult = freqMult
		# self.offset = offset
	
	# def solve(self):
		# solutions = []
		# numSolutions = 0.