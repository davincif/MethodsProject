class Func():
	function = None #The matematical description if the equation is continuous. type: function
	dataMass = None #The mass of points if the equation is discrete. type: [()]
	pvi = None #(a, b) --> y(a) = b

	def __init__(self, equation, pvi, discrete):
		if(discrete):
			print('not implemented yet')
			exit()
		else:
			self.function = equation

		self.pvi = pvi

	def compute(self, variables):
		return self.function(variables)
