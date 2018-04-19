# Euler Formula: yn+1 = yn + h*f(xn, yn)

class Euler():
	h = None
	dydx = None
	hf = None   # final h
	hi = None   # initial h
	__y0 = None

	outfile = None  # output file
	pmass = None    # poit mass

	def __init__(self, dydx, h, hf, hi):
		try:
			self.outfile = open('outputs/euler', 'w')
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
		while(tn < self.hf):
			self.yn = self.yn + self.h*self.dydx.compute(tn)

			tn += self.h

		return self.yn

	def write(self):
		pass
