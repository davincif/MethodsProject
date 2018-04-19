# Modified Euler Formula: yn+1 = yn + h/2 * (f(xn, yn) + f(x(n+1), y(n+1)))

class OptEuler():
	h = None
	dydx = None
	hf = None   # final h
	hi = None   # initial h
	__y0 = None

	outfile = None  # output file
	pmass = None    # poit mass

	def __init__(self, dydx, h, hf, hi):
		try:
			self.outfile = open('outputs/optEuler', 'w')
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
		tn = [self.hi, self.hi]
		last = [self.dydx.compute(tn[0]), None]
		while(tn[0] < self.hf):
			last[1] = last[0]
			last[0] = self.dydx.compute(tn[1])
			self.yn = self.yn + (self.h/2)*(last[0] + last[1])

			tn[1] = tn[0]
			tn[0] += self.h

		return self.yn

	def write(self):
		pass
