from abc import ABCMeta, abstractmethod
import math

class Equation:
	
	__metaclass__ = ABCMeta
	
	# abstract method that must be overridden for a class to work
	@abstractmethod
	def solve(self):
		pass
	
	@abstractmethod
	def toString(self):
		pass


# f(x) = mx + b
# this version solves for x
class LinearEquationX(Equation):
	
	def __init__( self, m, b, fx ):
		self.slope = m
		self.offset = b
		self.known = fx
	
	def solve(self):
		return ( ( self.known - self.offset ) / self.slope )
	
	def toString(self):
		return '{0} = {1}*x + {2}'.format( *(self.known, self.slope, self.offset) )


# f(x) = mx + b
# this version solves for f(x)
class LinearEquationY(Equation):
	
	def __init__( self, m, b, x ):
		self.slope = m
		self.offset = b
		self.known = x
	
	def solve(self):
		return ( self.known * self.slope + self.offset )
	
	def toString(self):
		return 'f(x) = {0}*{1} + {2}'.format( *(self.slope, self.known, self.offset) )


# (x-h)^2 + (y-k)^2 = r^2
# solves for y with a vertical line
class CircleVerticleLineEquation(Equation):
	
	def __init__( self, h, k, r, lineX ):
		self.h = h
		self.k = k
		self.radius = r
		self.lineX = lineX
	
	def solve(self):
		term = math.sqrt( self.radius**2 - self.lineX**2 + 2*self.lineX*self.h - self.h**2 )
		return ( self.k + term, self.k - term )
	
	def toString(self):
		return '({0} - {1})^2 + (y-{2})^2 = {3}^2'.format( *(self.lineX, self.h, self.k, self.radius) )

# (x-h)^2 + (y-k)^2 = r^2
# solves for x with a horizontal line
class CircleHorizontalLineEquation(Equation):
	
	def __init__( self, h, k, r, lineY ):
		self.h = h
		self.k = k
		self.radius = r
		self.lineY = lineY
	
	def solve(self):
		term = math.sqrt( self.radius**2 - self.lineY**2 + 2*self.lineY*self.k - self.k**2 )
		return ( self.h + term, self.h - term )
	
	def toString(self):
		return '(x - {0})^2 + ({1}-{2})^2 = {3}^2'.format( *(self.h, self.lineY, self.k, self.radius) )

		
# an equation of the type f(x) = mx^2 + b
# this solves for x
class QuadraticEquationX(Equation):
	
	def __init__(self, m, b, fx):
		self.slope = m
		self.offset = b
		self.known = fx
		
	def solve(self):
		temp = math.sqrt(((self.known - self.offset) / self.slope))
		return (temp, -temp)
		
	def toString(self):
		return '{0} = {1}*x ^2 + {2}'.format( *( self.known, self.slope, self.offset) )

		
# an equation of the type f(x) = mx^2 + b
# this solves for f(x)
class QuadraticEquationY(Equation):

	def __init__(self, m, b, x):
		self.slope = m
		self.offset = b
		self.known = x
		
	def solve(self):
		return ( (self.known ** 2) * self.slope + self.offset )
		
	def toString(self):
		return 'f(x) = {0}*{1}^2 + {2}'.format( *( self.slope, self.known, self.offset) )

		
# class SineSolutionEquation(Equation):
	
	# def __init__( self, start, end, freqMult, offset ):
		# self.min = start
		# self.max = end
		# self.freqMult = freqMult
		# self.offset = offset
	
	# def solve(self):
		# solutions = []
		# numSolutions = 0.
