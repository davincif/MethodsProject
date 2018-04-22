from enum import Enum

class MethodsType(Enum):
	ALL = 0
	EULER = 1
	EULERBACKWARD = 2
	EULERMOD = 3
	RUNGEKUTTA = 4
	ADAMBASHFORD = 5
	ADAMOULTON = 6
	DIFINV = 7 #Diferenciação Inversa
