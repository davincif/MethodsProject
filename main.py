#python3
import sys
try:
	assert sys.version_info >= (3,5)
except Exception as exc:
	print("you must have python version 3.5 or higher.\nCurrent is: " + str(sys.version))
	exit()
import json

from sympy.core import sympify

dydt = None #y'
Y = None #y
T = None #t

#1 - t + 4*y
def main():
	global dydt
	global Y
	global T

	dydt, Y, T, y0, yy0, h, steps = readEntry()

	#run methods
	methods = {}
	methods['euler'] = euler(steps, h, y0, yy0, difeq)
	methods['eulerBackward'] = eulerBackward(steps, h, y0, yy0, difeq)
	methods['eulerMod'] = eulerMod(steps, h, y0, yy0, difeq)
	methods['rungeKutta'] = rungeKutta(steps, h, y0, yy0, difeq)
	methods['adamBashford_2'] = adamBashford_2(steps, h, y0, yy0, difeq, rungeKutta)
	methods['adamBashford_3'] = adamBashford_3(steps, h, y0, yy0, difeq, rungeKutta)
	methods['adamBashford_4'] = adamBashford_4(steps, h, y0, yy0, difeq, rungeKutta)
	print(json.dumps(methods, indent=4)) #sort_keys=True

#differential equation
def difeq(t, y):
	global dydt
	global Y
	global T

	return dydt.subs({Y: y, T: t}).evalf()

def euler(qtd, h, hi, yhi, func):
	yn = yhi
	tn = hi
	table = []
	while(qtd > 0):
		table.append([tn, float(yn)])
		yn = (yn + h*func(tn, yn)).evalf()
		tn += h
		qtd -= 1

	return table

def eulerBackward(qtd, h, hi, yhi, func):
	h = float(h)
	yn = yhi
	tn = hi
	table = []
	while(qtd > 0):
		table.append([tn, float(yn)])
		byn = yn + h*func(tn, yn)
		yn = yn + h*func(tn+h, byn)
		tn += h
		qtd -= 1

	return table

def eulerMod(qtd, h, hi, yhi, func):
	yn = yhi
	tn = hi
	table = []
	while(qtd > 0):
		table.append([tn, float(yn)])
		byn = yn + h*func(tn, yn)
		yn = yn + 0.5*h*(func(tn, yn) + func(tn+h, byn))
		tn += h
		qtd -= 1

	return table

def rungeKutta(qtd, h, hi, yhi, func):
	yn = yhi
	tn = hi
	k1 = k2 = k3 = k4 = None
	table = []
	while(qtd > 0):
		table.append([tn, float(yn)])
		k1 = func(tn, yn)
		k2 = func(tn + 0.5*h, yn + 0.5*h*k1)
		k3 = func(tn + 0.5*h, yn + 0.5*h*k2)
		k4 = func(tn + h, yn + h*k3)
		yn = yn + (h/6)*(k1 + 2*(k2+k3) + k4)
		tn += h
		qtd -= 1

	return table

def adamBashford_2(qtd, h, hi, yhi, func, meth):
	lastp = [x[1] for x in meth(2, h, hi, yhi, func)] #lastp == last points
	yn = yhi
	tn0 = hi
	tn1 = hi+h
	table = [[tn0, lastp[0]], [tn1, lastp[1]]]
	qtd -= 2
	while(qtd > 0):
		yn = lastp[1] + 0.5*h * (3*func(tn1, lastp[1]) - func(tn0, lastp[0]))
		lastp[0] = lastp[1]
		lastp[1] = yn
		tn0 = tn1
		tn1 += h
		qtd -= 1
		table.append([tn1, float(yn)])

	return table

def adamBashford_3(qtd, h, hi, yhi, func, meth):
	lastp = [x[1] for x in meth(3, h, hi, yhi, func)] #lastp == last points
	yn = yhi
	tn0 = hi
	tn1 = hi+h
	tn2 = tn1+h
	table = [[tn0, lastp[0]], [tn1, lastp[1]], [tn2, lastp[2]]]
	qtd -= 3
	while(qtd > 0):
		yn = lastp[2] + h*(23*func(tn2, lastp[2]) - 16*func(tn1, lastp[1]) + 5*func(tn0, lastp[0]))/12
		lastp[0] = lastp[1]
		lastp[1] = lastp[2]
		lastp[2] = yn
		tn0 = tn1
		tn1 = tn2
		tn2 += h
		qtd -= 1
		table.append([tn2, float(yn)])

	return table

def adamBashford_4(qtd, h, hi, yhi, func, meth):
	lastp = [x[1] for x in meth(4, h, hi, yhi, func)] #lastp == last points
	yn = yhi
	tn0 = hi
	tn1 = hi+h
	tn2 = tn1+h
	tn3 = tn2+h
	table = [[tn0, lastp[0]], [tn1, lastp[1]], [tn2, lastp[2]], [tn3, lastp[3]]]
	qtd -= 4
	while(qtd > 0):
		yn = lastp[3] + h*(55*func(tn3, lastp[3]) - 59*func(tn2, lastp[2]) + 37*func(tn1, lastp[1]) - 9*func(tn0, lastp[0]))/24
		lastp[0] = lastp[1]
		lastp[1] = lastp[2]
		lastp[2] = lastp[3]
		lastp[3] = yn
		tn0 = tn1
		tn1 = tn2
		tn2 = tn3
		tn3 += h
		qtd -= 1
		table.append([tn3, float(yn)])

	return table

def adamMoulton():
	pass

def difInv():
	#Diferenciação Inversa
	pass


def readEntry():
	#read the differential equation
	while True:
		try :
			Y = sympify('y')
			T = sympify('t')
			print("Type the Differential Equation")
			print("dy/dx = ", end="")
			dydt = sympify(input(), evaluate=True)

			qtdvar = 0
			for symb in dydt.atoms():
				if(symb == Y):
					Y = symb
				elif(symb == T):
					T = symb

				if(type(symb) == type(Y)):
					qtdvar += 1

			# 1-t+4*y
			if (qtdvar < 0 or qtdvar > 2):
				raise Exception("There must be >= 0 and <= 2 variables at maximum: this expretion has " + str(qtdvar))

			print('Expression: ' + str(dydt))

			break
		except Exception as exp:
			print(exp, end='\n\n')
			print("Try again")

	#read the y0 of the inicial value (PVI, in portuguese)
	while True:
		try:
			print('Type the Inicial Value')
			print('initial y = ', end='')
			y0 = float(input())
			break
		except Exception as exp:
			print(exp, end='\n\n')
			print("Try again")

	#read the y(y0) of the inicial value (PVI, in portuguese)
	while True:
		try:
			print('y(' + str(y0) + ') = ', end='')
			yy0 = float(input())
			break
		except Exception as exp:
			print(exp, end='\n\n')
			print("Try again")

	#read the step size: h
	while True:
		try:
			print("Type the steps size. The 'h'")
			print('h = ', end='')
			h = float(input())
			break
		except Exception as exp:
			print(exp, end='\n\n')
			print("Try again")

	#read the step amount
	while True:
		try:
			print("Type the steps amount")
			print('steps = ', end='')
			steps = float(input())
			break
		except Exception as exp:
			print(exp, end='\n\n')
			print("Try again")

	return dydt, Y, T, y0, yy0, h, steps

if __name__ == '__main__':
	main()
