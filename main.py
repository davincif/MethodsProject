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
	meth = None

	while True:
		op = 'n' #option

		#read what method the user wants to use
		mop, dop, mop2 = methodMenu() #mop = method option | dop = degree option
		if(mop == None and dop == None):
			print('\nthank you, hope you enjoyed!')
			break

		if(not methods.dydt is None):
			op = ''
			while(op != 'y' and op != 'n'):
				print("Same ODE, h, y(0), y and steps?\n(y|n): ", end='')
				op = input()

				if(op != 'y' and op != 'n'):
					print("say 'y' or 'n', for yes or no", end='\n\n')

		if(op == 'n'):
			#read user entry about the method
			meth = {}
			methods.dydt, methods.Y, methods.T, y0, yy0, h, steps = readEntry()

		#run choices
		runChoices(meth, mop, mop2, dop, steps, h, y0, yy0)
		print(json.dumps(meth, indent=4)) #sort_keys=True


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
				elif(type(symb) == type(Y)):
					raise Exception("there must be only t's and y's as variables in the expression")

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
			print('initial t = ', end='')
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
	type2 = None

	while True:
		op, valid = printMenu([])
		type, degree = getChosenMethod(op, valid)

		if(not type is None or degree == None):
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

		op, valid = printMenu([MethodsType.ALL, MethodsType.ADAMBASHFORD, 'quit'])
		type2 = getChosenMethod(op, valid)

	return type, degree, type2

def runChoices(dict2save, method, method2, degree, steps, h, y0, yy0):
	func = MethodsType.getFunction(method2, 0)

	for meth in MethodsType.getFunction(method, degree):
		if(MethodsType.getTypeByFunction(meth) == MethodsType.ADAMBASHFORD):
			dict2save[MethodsType.getNameByFunction(meth)] = meth(steps, h, y0, yy0, func[0])
		else:
			dict2save[MethodsType.getNameByFunction(meth)] = meth(steps, h, y0, yy0)


def getChosenMethod(userStr, valid):
	type = None

	try:
		userStr = int(float(userStr))

		if(userStr in valid):
			if(userStr == 0):
				type = MethodsType.ALL
			elif(userStr == 1):
				type = MethodsType.EULER
			elif(userStr == 2):
				type = MethodsType.EULERBACKWARD
			elif(userStr == 3):
				type = MethodsType.EULERMOD
			elif(userStr == 4):
				type = MethodsType.RUNGEKUTTA
			elif(userStr == 5):
				type = MethodsType.ADAMBASHFORD
			elif(userStr == 6):
				type = MethodsType.ADAMOULTON
			elif(userStr == 7):
				type = MethodsType.DIFINV
			elif(userStr == 99):
				type = degree = None
			else:
				raise IndexError('Option out of range')
		else:
			raise IndexError('Option not avaliable')

	except IndexError as exp:
		print(exp)
		print("Try again", end='\n\n')
	except Exception as exp:
		userStr = userStr.upper()

		if(userStr == "ALL"):
			type = MethodsType.ALL
		elif(userStr == "EULER"):
			type = MethodsType.EULER
		elif(userStr == "EULER BACKWARD" or userStr == "BACKWARD EULER" or userStr == "B EULER" or userStr == "EULER B"):
			type = MethodsType.EULERBACKWARD
		elif(userStr == "EULER IMPROVED" or userStr == "IMPROVED EULER" or userStr == "EULER I" or userStr == "I EULER"):
			type = MethodsType.EULERMOD
		elif(userStr == "RUNGEKUTTA" or userStr == "RUNG-KUTTA" or userStr == "RUNG KUTTA"):
			type = MethodsType.RUNGEKUTTA
		elif(userStr == "ADAMBASHFORD" or userStr == "ADAM BASHFORD" or userStr == "ADAM B"):
			type = MethodsType.ADAMBASHFORD
		elif(userStr == "ADAMOULTON" or userStr == "ADA MOULTON" or userStr == "ADAM M"):
			type = MethodsType.ADAMOULTON
		elif(userStr == "INVERSE TRANSFORM SAMPLING" or userStr == "ITS"):
			type = MethodsType.DIFINV
		elif(userStr == "QUIT" or userStr == "Q"):
			type = degree = None
		else:
			print('Method not recognized, check your typing.')
			print("Try again", end='\n\n')

	return type, degree

def printMenu(notshow):
	valid = []

	print("type the name of the number of the option")
	print("What method do you wanna run?")
	if(not MethodsType.ALL in notshow):
		print("0. All")
		valid += [0]
	if(not MethodsType.EULER in notshow):
		print("1. Euler")
		valid += [1]
	if(not MethodsType.EULERBACKWARD in notshow):
		print("2. Euler Backward")
		valid += [2]
	if(not MethodsType.EULERMOD in notshow):
		print("3. Improved Euler")
		valid += [3]
	if(not MethodsType.RUNGEKUTTA in notshow):
		print("4. Runge-Kutta")
		valid += [4]
	if(not MethodsType.ADAMBASHFORD in notshow):
		print("5. Adams Bashford")
		valid += [5]
	if(not MethodsType.ADAMOULTON in notshow):
		print("6. Adams Moulton")
		valid += [6]
	if(not MethodsType.DIFINV in notshow):
		print("7. Inverse Transform Sampling (ITS)")
		valid += [7]
	if(not 'quit' in notshow):
		print("99. quit (q)")
		valid += [99]
	op = input()

	return op, valid

if __name__ == '__main__':
	main()
