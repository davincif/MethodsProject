from sympy.core import sympify

#x + 1 + y**3 - 2*x
def main():
	#read function
	eq = None
	var_qtd = []
	while True:
		try :
			aux = sympify('aux')
			print("dy/dx = ", end="")
			eq = sympify(input(), evaluate=True)
			for symb in eq.atoms():
				if(type(symb) == type(aux)):
					var_qtd += [symb]
			print('\nWhat was read:')
			print('Expression: ' + str(eq))
			print('Identified variables: ' + str(var_qtd), end='\n\n')

			break
		except ValueError as exp:
			print(exp, end='\n\n')
			print("Try again")

	#run methods
	# euler(eq, )


if __name__ == '__main__':
	main()

def euler(dydx, h, hf, hi, yhi):
	yn = yhi
	hn = hi
	yvar = sympify('y')
	aux = None
	while(hn < hf):
		hn += h
		for variable in var_qtd:
			if(variable == yvar):
				aux = dydx.subs(variable, yn)
			else:
				aux = dydx.subs(variable, hn)
		y = yn + h*aux
