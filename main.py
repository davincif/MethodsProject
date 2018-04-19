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
	methods['euler'] = euler(6, 0.05, 0, 1, funczinha)
	methods['eulerBackward'] = eulerBackward(6, 0.05, 0, 1, funczinha)
	methods['eulerMod'] = eulerMod(16, 0.025, 0, 1, funczinha)
	print(methods)

def funczinha(t, y):
	# aux = aux.subs({mvar[0]: hn, mvar[1]: }).evalf()
	return 1 - t + 4*y

def euler(qtd, h, hi, yhi, func):
	yn = yhi
	tn = hi
	while(qtd > 0):
		yn = yn + h*func(tn, yn)
		tn += h
		qtd -= 1

	return yn

def eulerBackward(qtd, h, hi, yhi, func):
	yn = yhi
	tn = hi
	while(qtd > 0):
		print(tn, "|", yn)
		byn = yn + h*func(tn, yn)
		yn = yn + h*func(tn+h, byn)
		tn += h
		qtd -= 1

	return yn

def eulerMod(qtd, h, hi, yhi, func):
	yn = yhi
	tn = hi
	while(qtd > 0):
		byn = yn + h*func(tn, yn)
		yn = yn + (h/2)*(func(tn, yn) + func(tn+h, byn))
		tn += h
		qtd -= 1

	return yn

def rungeKutta():
	pass

def adamBashford():
	pass

def adamMoulton():
	pass

def difInv():
	#Diferenciação Inversa
	pass


if __name__ == '__main__':
	main()
