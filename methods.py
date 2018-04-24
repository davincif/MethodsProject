dydt = None #y'
Y = None #y
T = None #t

def difeq(t, y):
	#differential equation
	global dydt
	global Y
	global T

	return dydt.subs({Y: y, T: t}).evalf()

def euler(qtd, h, hi, yhi):
	yn = yhi
	tn = hi
	table = []
	while(qtd > 0):
		table.append([tn, float(yn)])
		yn = (yn + h*difeq(tn, yn)).evalf()
		tn += h
		qtd -= 1

	return table

def eulerBackward(qtd, h, hi, yhi):
	h = float(h)
	yn = yhi
	tn = hi
	table = []
	while(qtd > 0):
		table.append([tn, float(yn)])
		byn = yn + h*difeq(tn, yn)
		yn = yn + h*difeq(tn+h, byn)
		tn += h
		qtd -= 1

	return table

def eulerMod(qtd, h, hi, yhi):
	yn = yhi
	tn = hi
	table = []
	while(qtd > 0):
		table.append([tn, float(yn)])
		byn = yn + h*difeq(tn, yn)
		yn = yn + 0.5*h*(difeq(tn, yn) + difeq(tn+h, byn))
		tn += h
		qtd -= 1

	return table

def rungeKutta(qtd, h, hi, yhi):
	yn = yhi
	tn = hi
	k1 = k2 = k3 = k4 = None
	table = []
	while(qtd > 0):
		table.append([tn, float(yn)])
		k1 = difeq(tn, yn)
		k2 = difeq(tn + 0.5*h, yn + 0.5*h*k1)
		k3 = difeq(tn + 0.5*h, yn + 0.5*h*k2)
		k4 = difeq(tn + h, yn + h*k3)
		yn = yn + (h/6)*(k1 + 2*(k2+k3) + k4)
		tn += h
		qtd -= 1

	return table

def adamBashford_2(qtd, h, hi, yhi, meth):
	lastp = [x[1] for x in meth(2, h, hi, yhi)] #lastp == last points
	yn = yhi
	tn0 = hi
	tn1 = hi+h
	table = [[tn0, lastp[0]], [tn1, lastp[1]]]
	qtd -= 2
	while(qtd > 0):
		yn = lastp[1] + 0.5*h * (3*difeq(tn1, lastp[1]) - difeq(tn0, lastp[0]))
		lastp[0] = lastp[1]
		lastp[1] = yn
		tn0 = tn1
		tn1 += h
		qtd -= 1
		table.append([tn1, float(yn)])

	return table

def adamBashford_3(qtd, h, hi, yhi, meth):
	lastp = [x[1] for x in meth(3, h, hi, yhi)] #lastp == last points
	yn = yhi
	tn0 = hi
	tn1 = hi+h
	tn2 = tn1+h
	table = [[tn0, lastp[0]], [tn1, lastp[1]], [tn2, lastp[2]]]
	qtd -= 3
	while(qtd > 0):
		yn = lastp[2] + h*(23*difeq(tn2, lastp[2]) - 16*difeq(tn1, lastp[1]) + 5*difeq(tn0, lastp[0]))/12
		lastp[0] = lastp[1]
		lastp[1] = lastp[2]
		lastp[2] = yn
		tn0 = tn1
		tn1 = tn2
		tn2 += h
		qtd -= 1
		table.append([tn2, float(yn)])

	return table

def adamBashford_4(qtd, h, hi, yhi, meth):
	lastp = [x[1] for x in meth(4, h, hi, yhi)] #lastp == last points
	yn = yhi
	tn0 = hi
	tn1 = hi+h
	tn2 = tn1+h
	tn3 = tn2+h
	table = [[tn0, lastp[0]], [tn1, lastp[1]], [tn2, lastp[2]], [tn3, lastp[3]]]
	qtd -= 4
	while(qtd > 0):
		yn = lastp[3] + h*(55*difeq(tn3, lastp[3]) - 59*difeq(tn2, lastp[2]) + 37*difeq(tn1, lastp[1]) - 9*difeq(tn0, lastp[0]))/24
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

def adamMoulton_2(qtd, h, hi, yhi):
	pass

def adamMoulton_3(qtd, h, hi, yhi):
	pass

def adamMoulton_4(qtd, h, hi, yhi):
	lastp = [x[1] for x in adamBashford_4(4, h, hi, yhi, rungeKutta)] #lastp == last points
	yn = yhi
	tn = hi
	table = [[tn, lastp[0]], [tn+h, lastp[1]], [tn+2*h, lastp[2]], [tn+3*h, lastp[3]]]
	tn += 3*h
	qtd -= 4
	while(qtd > 0):
		yn = difeq(tn + h, lastp[3])
		lastp[0] = lastp[1]
		lastp[1] = lastp[2]
		lastp[2] = lastp[3]
		lastp[3] = yn
		tn += h
		qtd -= 1
		table.append([tn, float(yn)])
		lastp = [x[1] for x in adamBashford_4(4, h, hi, yhi, lambda qtd, h, hi, yhi : __methodMock(qtd, h, hi, yhi, list2return=table))]

	return table

def difInv():
	#Diferenciação Inversa
	pass

def __methodMock(qtd, h, hi, yhi, list2return):
	return list2return