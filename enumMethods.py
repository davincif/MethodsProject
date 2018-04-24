from enum import Enum
import methods

class MethodsType(Enum):
	ALL = 0
	EULER = 1
	EULERBACKWARD = 2
	EULERMOD = 3
	RUNGEKUTTA = 4
	ADAMBASHFORD = 5
	ADAMOULTON = 6
	DIFINV = 7 #Diferenciação Inversa

	def getFunction(enum, degree):
		func = []

		if(enum == MethodsType.EULER or enum == MethodsType.ALL):
			func += [methods.euler]

		if(enum == MethodsType.EULERBACKWARD or enum == MethodsType.ALL):
			func += [methods.eulerBackward]

		if(enum == MethodsType.EULERMOD or enum == MethodsType.ALL):
			func += [methods.eulerMod]

		if(enum == MethodsType.RUNGEKUTTA or enum == MethodsType.ALL):
			func += [methods.rungeKutta]

		if(enum == MethodsType.ADAMBASHFORD or enum == MethodsType.ALL):
			if(degree == 0):
				func += [methods.euler]

			if(degree == 2 or degree == -1):
				func += [methods.adamBashford_2]

			if(degree == 3 or degree == -1):
				func += [methods.adamBashford_3]

			if(degree == 4 or degree == -1):
				func += [methods.adamBashford_4]
		if(enum == MethodsType.ADAMOULTON or enum == MethodsType.ALL):
			if(degree == 0):
				func += [methods.eulerBackward]

			if(degree == 2 or degree == -1):
				func += [methods.adamMoulton_2]

			if(degree == 3 or degree == -1):
				func += [methods.adamMoulton_3]

			if(degree == 4 or degree == -1):
				func += [methods.adamMoulton_4]
		if(enum == MethodsType.DIFINV or enum == MethodsType.ALL):
			if(degree == 2 or degree == -1):
				func += [methods.difInv]

			if(degree == 3 or degree == -1):
				func += [methods.difInv]

			if(degree == 4 or degree == -1):
				func += [methods.difInv]


		return func

	def getNameByFunction(func):
		if(func == methods.euler):
			return 'euler'
		elif(func == methods.eulerBackward):
			return 'eulerBackward'
		elif(func == methods.eulerMod):
			return 'eulerMod'
		elif(func == methods.rungeKutta):
			return 'rungeKutta'
		elif(func == methods.adamBashford_2):
			return 'adamBashford_2'
		elif(func == methods.adamBashford_3):
			return 'adamBashford_3'
		elif(func == methods.adamBashford_4):
			return 'adamBashford_4'
		elif(func == methods.adamMoulton_2):
			return 'adamMoulton_2'
		elif(func == methods.adamMoulton_3):
			return 'adamMoulton_3'
		elif(func == methods.adamMoulton_4):
			return 'adamMoulton_4'
		elif(func == methods.difInv):
			return 'defInv'
		else:
			return ''

	def getName(enum, degree):
		if(enum == MethodsType.EULER):
			return 'euler'
		elif(enum == MethodsType.EULERBACKWARD):
			return 'eulerBackward'
		elif(enum == MethodsType.EULERMOD):
			return 'eulerMod'
		elif(enum == MethodsType.RUNGEKUTTA):
			return 'rungeKutta'
		elif(enum == MethodsType.ADAMBASHFORD):
			if(degree == 0):
				return 'adamBashford_0'
			if(degree == 2):
				return 'adamBashford_2'
			if(degree == 3):
				return 'adamBashford_3'
			if(degree == 4):
				return 'adamBashford_4'
		elif(enum == MethodsType.ADAMOULTON):
			if(degree == 0):
				return 'adamMoulton_0'
			if(degree == 2):
				return 'adamMoulton_2'
			if(degree == 3):
				return 'adamMoulton_3'
			if(degree == 4):
				return 'adamMoulton_4'
		elif(enum == MethodsType.DIFINV):
			if(degree == 0):
				return 'defInv'
			if(degree == 2):
				return 'defInv'
			if(degree == 3):
				return 'defInv'
			if(degree == 4):
				return 'defInv'

	def getTypeByFunction(func):
		if(func == methods.euler):
			return MethodsType.EULER
		elif(func == methods.eulerBackward):
			return MethodsType.EULERBACKWARD
		elif(func == methods.eulerMod):
			return MethodsType.EULERMOD
		elif(func == methods.rungeKutta):
			return MethodsType.RUNGEKUTTA
		elif(func == methods.adamBashford_2 or func == methods.adamBashford_3 or func == methods.adamBashford_4):
			return MethodsType.ADAMBASHFORD
		elif(func == methods.adamMoulton_2 or func == methods.adamMoulton_3 or func == methods.adamMoulton_4):
			return MethodsType.ADAMOULTON
		elif(func == methods.DIFINV):
			return MethodsType.DIFINV
