#python3
import sys
try:
	assert sys.version_info >= (3,5)
except Exception as exc:
	print("you must have python version 3.5 or higher.\nCurrent is: " + str(sys.version))
	exit()
from pprint import pprint

from sympy.core import sympify
from sympy import lambdify

dydx = None
Y = None
X = None

#x + 1 + y**3 - 2*x
def main():
	global dydx
	global mvar

	#read function
	while True:
		try :
			Y = sympify('y')
			print("dy/dx = ", end="")
			dydx = sympify(input(), evaluate=True)
			if (len(dydx.atoms()) > 2):
				raise("There must be 2 variables at maximum")
			for symb in dydx.atoms():
				if(symb == Y):
					Y = symb
				else:
					X = symb
			print('Expression: ' + str(dydx))

			break
		except ValueError as exp:
			print(exp, end='\n\n')
			print("Try again")

	#run methods
	methods = {}
	methods['euler'] = euler(6, 0.05, 0, 1.0, funczinha)
	methods['eulerBackward'] = eulerBackward(6, 0.05, 0, 1.0, funczinha)
	methods['eulerMod'] = eulerMod(16, 0.025, 0, 1.0, funczinha)
	methods['rungeKutta'] = rungeKutta(16, 0.025, 0, 1.0, funczinha)
	# methods['adamBashford'] = adamBashford(10, 0.025, 0, 1.0, funczinha)
	pprint(methods)

def funczinha(t, y):
	# aux = aux.subs({mvar[0]: hn, mvar[1]: }).evalf()
	return 1 - t + 4*y

def euler(qtd, h, hi, yhi, func):
	yn = yhi
	tn = hi
	table = []
	while(qtd > 0):
		table.append([tn, yn])
		yn = yn + h*func(tn, yn)
		tn += h
		qtd -= 1

	return table

def eulerBackward(qtd, h, hi, yhi, func):
	h = float(h)
	yn = yhi
	tn = hi
	table = []
	while(qtd > 0):
		table.append([tn, yn])
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
		table.append([tn, yn])
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
		table.append([tn, yn])
		k1 = func(tn, yn)
		k2 = func(tn + 0.5*h, yn + 0.5*h*k1)
		k3 = func(tn + 0.5*h, yn + 0.5*h*k2)
		k4 = func(tn + h, yn + h*k3)
		yn = yn + (h/6)*(k1 + 2*(k2+k3) + k4)
		tn += h
		qtd -= 1

	return table

def adamBashford(qtd, h, hi, yhi, func):
	yn = yhi
	tn = hitable = []
	while(qtd > 0):
		print(tn, "|", yn)
		tn += h
		qtd -= 1

	return table

def adamMoulton():
	pass

def difInv():
	#Diferenciação Inversa
	pass


if __name__ == '__main__':
	main()
