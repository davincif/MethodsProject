# Runge-Kutta Formula: yn+1 = yn + h/6 * (k1 + 2k2 + 2k3 + k4)
# k1 = f(tn, yn)
# k2 = f(tn + h/2, yn + h/2 * k1)
# k3 = f(tn + h/2, yn + h/2 * k2)
# k4 = f(tn + h, yn + h*k3)

class RungeKutta():
	h = None
	dydx = None
	hf = None   # final h
	hi = None   # initial h
	__y0 = None

	outfile = None  # output file
	pmass = None    # poit mass

	def __init__(self, dydx, h, hf, hi):
		try:
			self.outfile = open('outputs/runge_kutta', 'w')
		except Exception as exp:
			exit(exp);

		self.h = h
		self.dydx = dydx
		self.hf = hf
		self.hi = hi
		self.__y0 = dydx.pvi[1]

	def __del__(self):
		self.outfile.close()

	def compute(self):
		#clean
		self.yn = None

		self.yn = self.__y0
		tn = self.hi
		k1 = k2 = k3 = k4 = None
		while(tn < self.hf):
			k1 = self.dydx.compute(tn)
			k2 = self.dydx.compute(tn/2)
			k3 = self.dydx.compute(tn/2)
			k4 = self.dydx.compute(tn)
			self.yn = self.yn + (self.h/2) * (k1 + 2*(k2 + k3) + k4)

			tn += self.h

		return self.yn

	def write(self):
		pass
