from indata.func import Func
from indata.funcPool import y1, y1_pvi
from methods.euler import Euler
from methods.optEuler import OptEuler
from methods.runge_kutta import RungeKutta

def main():
	methods = {}
	dydx = Func(y1, y1_pvi(), False)

	euler = Euler(dydx, 0.025, 1.1, 1)
	optEuler = OptEuler(dydx, 0.025, 1.1, 1)
	rkutta = RungeKutta(dydx, 0.025, 1.1, 1)

	methods['euler'] = euler.compute()
	methods['optEuler'] = optEuler.compute()
	methods['runge_kutta'] = rkutta.compute()

	print(methods)


if __name__ == '__main__':
	main()
