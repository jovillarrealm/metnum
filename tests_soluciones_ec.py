
from soluciones_ec import *


def e(exp): return 10**exp
f = "90*(x+90)*(x+27)*(x+40) - 50_000_000"
f = "x**3 - 7.51*x**2 + 18.4239*x - 14.8331"
h = "(x+1)*(x-10)"
dx = .01
tol = 0.5*e(-5)
x_i = 0
n_max = 100000

x = symbols("x")
#x_i, x_f =busqueda_incremental(f, dx, x_i, n_max)
#print(bisect(x_i,x_f,f,tol))
#print(newton(f,x_i,tol,n_max))
#print(bisect(-1, 20, f, .002))


#print(diff(sympify("x**3-x**2-x+1+sin(x-1)**2"),symbols("x")))
#print(diff(sympify("x**3-x**2-x+1+sin(x-1)**2"),symbols("x"),symbols("x")))
#print(busqueda_incremental("x**3-x**2/sqrt(2)-5",-0.3,0,1_000_000))

#print(diff(sympify('(1/5)'),x))
#print(multiplicidad("sin(x)**5*(x**2-2)", 0))
#print(multiplicidad("(sin(x)**5*(x**2-2))/(2*x*sin(x)**5 + 5*(x**2 - 2)*sin(x)**4*cos(x))",0))
#print(bisect(0.8,1.1,"(x**4-x**3-x**2+x)/(4*x**3 - 3*x**2 - 2*x + 1)",0.001))