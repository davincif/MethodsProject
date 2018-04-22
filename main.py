#python3

#system imports
import sys
try:
	assert sys.version_info >= (3,5)
except Exception as exc:
	print("you must have python version 3.5 or higher.\nCurrent is: " + str(sys.version))
	exit()
print('loading...', end='\n\n')
import json

#third party libraries import
from sympy.core import sympify

#local imports
import methods
from enumMethods import MethodsType


#1 - t + 4*y
def main():
	meth = {}

	#read what method the user wants to use
	mop, dop = methodMenu() #mop = method option | dop = degree option

	#read user entry about the method
	methods.dydt, methods.Y, methods.T, y0, yy0, h, steps = readEntry()

	#run choices
	runChoices(meth, mop, dop, steps, h, y0, yy0)


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

def runChoices(dict2save, method, degree, steps, h, y0, yy0):

	#run chosen methods
	if(method == MethodsType.EULER or method == MethodsType.ALL):
		dict2save['euler'] = methods.euler(steps, h, y0, yy0)

	if(method == MethodsType.EULERBACKWARD or method == MethodsType.ALL):
		dict2save['eulerBackward'] = methods.eulerBackward(steps, h, y0, yy0)

	if(method == MethodsType.EULERMOD or method == MethodsType.ALL):
		dict2save['eulerMod'] = methods.eulerMod(steps, h, y0, yy0)

	if(method == MethodsType.RUNGEKUTTA or method == MethodsType.ALL):
		dict2save['rungeKutta'] = methods.rungeKutta(steps, h, y0, yy0)

	if((method == MethodsType.ADAMBASHFORD or method == MethodsType.ALL) and degree == 0):
		dict2save['adamBashford_0'] = methods.euler(steps, h, y0, yy0)

	if((method == MethodsType.ADAMBASHFORD or method == MethodsType.ALL) and (degree == 2 or degree == -1)):
		dict2save['adamBashford_2'] = methods.adamBashford_2(steps, h, y0, yy0, methods.rungeKutta)

	if((method == MethodsType.ADAMBASHFORD or method == MethodsType.ALL) and (degree == 3 or degree == -1)):
		dict2save['adamBashford_3'] = methods.adamBashford_3(steps, h, y0, yy0, methods.rungeKutta)

	if((method == MethodsType.ADAMBASHFORD or method == MethodsType.ALL) and (degree == 4 or degree == -1)):
		dict2save['adamBashford_4'] = methods.adamBashford_4(steps, h, y0, yy0, methods.rungeKutta)

	print(json.dumps(dict2save, indent=4)) #sort_keys=True

if __name__ == '__main__':
	main()
