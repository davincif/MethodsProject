from sympy.core import sympify
from sympy import lambdify

dydx = None
var_qtd = []

#x + 1 + y**3 - 2*x
def main():
	global dydx
	global var_qtd

	#read function
	while True:
		try :
			aux = sympify('aux')
			print("dy/dx = ", end="")
			dydx = sympify(input(), evaluate=True)
			for symb in dydx.atoms():
				if(type(symb) == type(aux)):
					var_qtd += [symb]
			print('\nWhat was read:')
			print('Expression: ' + str(dydx))
			print('Identified variables: ' + str(var_qtd), end='\n\n')

			break
		except ValueError as exp:
			print(exp, end='\n\n')
			print("Try again")

	#run methods
	methods = {}
	methods['euler'] = euler(0.025, 1.1, 1, 1)
	print(methods)

def euler(h, hf, hi, yhi):
	global dydx
	global var_qtd

	yn = yhi
	hn = hi
	yvar = sympify('y')
	aux = dydx
	while(hn < hf):
		hn += h
		for variable in var_qtd:
			if(variable == yvar):
				aux = aux.subs(variable, yn).evalf()
			else:
				aux = aux.subs(variable, hn).evalf()
		yn = yn + h*aux

	return yn

def eulerMod():
	pass

def eulerBackward():
	pass

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
