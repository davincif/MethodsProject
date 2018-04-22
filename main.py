#python3
import sys
try:
	assert sys.version_info >= (3,5)
except Exception as exc:
	print("you must have python version 3.5 or higher.\nCurrent is: " + str(sys.version))
	exit()
import json

from sympy.core import sympify

from enumMethods import MethodsType

dydt = None #y'
Y = None #y
T = None #t

#1 - t + 4*y
def main():
	global dydt
	global Y
	global T
	methods = {}

	#read what method the user wants to use
	mop, dop = methodMenu() #mop = method option | dop = degree option

	#read user entry about the method
	dydt, Y, T, y0, yy0, h, steps = readEntry()

	#run choices
	runChoices(methods, mop, dop, dydt, Y, T, y0, yy0, h, steps)

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
			print("\nType the Differential Equation")
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
			print(exp)
			print("Try again", end='\n\n')

	#read the y0 of the inicial value (PVI, in portuguese)
	while True:
		try:
			print('Type the Inicial Value')
			print('initial y = ', end='')
			y0 = float(input())
			break
		except Exception as exp:
			print(exp)
			print("Try again", end='\n\n')

	#read the y(y0) of the inicial value (PVI, in portuguese)
	while True:
		try:
			print('y(' + str(y0) + ') = ', end='')
			yy0 = float(input())
			break
		except Exception as exp:
			print(exp)
			print("Try again", end='\n\n')

	#read the step size: h
	while True:
		try:
			print("Type the steps size. The 'h'")
			print('h = ', end='')
			h = float(input())
			break
		except Exception as exp:
			print(exp)
			print("Try again", end='\n\n')

	#read the step amount
	while True:
		try:
			print("Type the steps amount")
			print('steps = ', end='')
			steps = float(input())
			break
		except Exception as exp:
			print(exp)
			print("Try again", end='\n\n')

	return dydt, Y, T, y0, yy0, h, steps

def methodMenu():
	type = None
	degree = 0

	while True:
		print("type the name of the number of the option")
		print("What method do you wanna run?")
		print("0. All")
		print("1. Euler")
		print("2. Euler Backward")
		print("3. Improved Euler")
		print("4. Runge-Kutta")
		print("5. Adams Bashford")
		print("6. Adams Moulton")
		print("7. Inverse Transform Sampling (ITS)")
		op = input()

		try:
			op = int(float(op))

			if(op == 0):
				type = MethodsType.ALL
			elif(op == 1):
				type = MethodsType.EULER
			elif(op == 2):
				type = MethodsType.EULERBACKWARD
			elif(op == 3):
				type = MethodsType.EULERMOD
			elif(op == 4):
				type = MethodsType.RUNGEKUTTA
			elif(op == 5):
				type = MethodsType.ADAMBASHFORD
			elif(op == 6):
				type = MethodsType.ADAMOULTON
			elif(op == 7):
				type = MethodsType.DIFINV
			else:
				raise IndexError('Option out of range')

			break
		except IndexError as exp:
			print(exp)
			print("Try again", end='\n\n')
		except Exception as exp:
			op = op.upper()

			if(op == "ALL"):
				type = MethodsType.ALL
			elif(op == "EULER"):
				type = MethodsType.EULER
			elif(op == "EULER BACKWARD" or op == "BACKWARD EULER" or op == "B EULER" or op == "EULER B"):
				type = MethodsType.EULERBACKWARD
			elif(op == "EULER IMPROVED" or op == "IMPROVED EULER" or op == "EULER I" or op == "I EULER"):
				type = MethodsType.EULERMOD
			elif(op == "RUNGEKUTTA" or op == "RUNG-KUTTA" or op == "RUNG KUTTA"):
				type = MethodsType.RUNGEKUTTA
			elif(op == "ADAMBASHFORD" or op == "ADAM BASHFORD" or op == "ADAM B"):
				type = MethodsType.ADAMBASHFORD
			elif(op == "ADAMOULTON" or op == "ADA MOULTON" or op == "ADAM M"):
				type = MethodsType.ADAMOULTON
			elif(op == "INVERSE TRANSFORM SAMPLING" or op == "ITS"):
				type = MethodsType.DIFINV
			else:
				print('Method not recognized, check your typing.')
				print("Try again", end='\n\n')

			if(not type is None):
				break

	if(type == MethodsType.ADAMBASHFORD or type == MethodsType.ALL):
		while True:
				print('what the degree? (-1 for all)')
				print('\ndegree = ', end='')

				try:
					degree = int(float(input()))
					if(degree < -1 or degree > 4):
						raise IndexError('Option out of range')
					break
				except Exception as exp:
					print(exp)
					print("Try again", end='\n\n')

	return type, degree

def runChoices(dict2save, method, degree, dydt, Y, T, y0, yy0, h, steps):

	#run chosen methods
	if(method == MethodsType.EULER or method == MethodsType.ALL):
		dict2save['euler'] = euler(steps, h, y0, yy0, difeq)

	if(method == MethodsType.EULERBACKWARD or method == MethodsType.ALL):
		dict2save['eulerBackward'] = eulerBackward(steps, h, y0, yy0, difeq)

	if(method == MethodsType.EULERMOD or method == MethodsType.ALL):
		dict2save['eulerMod'] = eulerMod(steps, h, y0, yy0, difeq)

	if(method == MethodsType.RUNGEKUTTA or method == MethodsType.ALL):
		dict2save['rungeKutta'] = rungeKutta(steps, h, y0, yy0, difeq)

	if((method == MethodsType.ADAMBASHFORD or method == MethodsType.ALL) and degree == 0):
		dict2save['adamBashford_0'] = euler(steps, h, y0, yy0, difeq)

	if((method == MethodsType.ADAMBASHFORD or method == MethodsType.ALL) and (degree == 2 or degree == -1)):
		dict2save['adamBashford_2'] = adamBashford_2(steps, h, y0, yy0, difeq, rungeKutta)

	if((method == MethodsType.ADAMBASHFORD or method == MethodsType.ALL) and (degree == 3 or degree == -1)):
		dict2save['adamBashford_3'] = adamBashford_3(steps, h, y0, yy0, difeq, rungeKutta)

	if((method == MethodsType.ADAMBASHFORD or method == MethodsType.ALL) and (degree == 4 or degree == -1)):
		dict2save['adamBashford_4'] = adamBashford_4(steps, h, y0, yy0, difeq, rungeKutta)

	print(json.dumps(dict2save, indent=4)) #sort_keys=True

if __name__ == '__main__':
	main()
