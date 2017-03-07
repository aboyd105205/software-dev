import Equations as Eqs

# f(x) = mx + b
lineFunc = Eqs.LinearEquationY ( 10, 1, 15 )
print(lineFunc.toString())
print(lineFunc.solve())

# f(x) = mx^2 + b
quadFunc = Eqs.QuadraticEquationY ( 2, 3, 4 )
print(quadFunc.toString())
print(quadFunc.solve())

# (x-h)^2 + (y-k)^2 = r^2
circFunc = Eqs.CircleVerticleLineEquation ( 2, 2, 1, 2.5 )
print(circFunc.toString())
print(circFunc.solve())

