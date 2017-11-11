import sys
import math

class _CArgs:

	def __init__(self, argv):
		self.m_command = ''
		self.m_args = {}

		if len(argv) > 0:
			# 2017.11.2 Remove the first argument which always represents the program name
			argv.pop(0)

		if len(argv) > 0:
			# 2017.11.2 Pop the second argument which represents the command name(which operation users want to do)
			self.m_command = argv.pop(0).lower()

			# 2017.11.2 Generate the argument list
			key = None
			for arg in argv:
				if arg.startswith('-'):
					self.m_args[key] = None
					key = arg
				else:
					if key:
						self.m_args[key] = arg
						key = None

	def command(self):
		return self.m_command

	def has_param(self, param):
		return (param in self.m_args)

	def param(self, key, default):
		return self.m_args[key] if self.has_param(key) else default

class DataAnalysis:

	def __init__(self, data):
		self.m_data = data

	def check_data(self, checker):
		valid = True
		for num in self.m_data:
			if not checker(num):
				valid = False
				break
		return valid

	@staticmethod
	def checker_positive(num):
		return num > 0

	@staticmethod
	def checker_nonzero(num):
		return num != 0

	def data(self): return self.m_data

	def max(self): pass
	def min(self): pass

	def arithmetic_mean(self):
		result = None
		if len(self.m_data) > 0:
			sum = 0.0
			for num in self.m_data:
				sum += num
			result = sum / len(self.m_data)
		return result

	def geometric_mean(self):
		result = None
		if len(self.m_data) > 0 and self.check_data(DataAnalysis.checker_positive):
			product = 1.0
			for num in self.m_data:
				product *= num
			result **= (1 / len(self.m_data))
		return result

	def harmonic_mean(self):
		result = None
		if len(self.m_data) > 0 and self.check_data(DataAnalysis.checker_nonzero):
			sum = 0.0
			for num in self.m_data:
				sum += (1 / num)
			result = (len(self.m_data) / sum)
		return result

	def variance_sample(self):
		result = None
		count = len(self.m_data)
		if count > 1:
			am = self.arithmetic_mean()
			sum = 0.0
			for num in self.m_data:
				sum += ((num - am) ** 2)
			result = sum / (count - 1)
		return result

	def variance_population(self):
		result = None
		count = len(self.m_data)
		if count > 0:
			am = self.arithmetic_mean()
			sum = 0.0
			for num in self.m_data:
				sum += ((num - am) ** 2)
			result = sum / count
		return result

	def std_dev_sample(self):
		result = None
		count = len(self.m_data)
		if count > 0:
			vars = self.variance_sample() / count
			result = vars ** (1 / 2)
		return result

	def std_dev_population(self):
		result = None
		if count > 0:
			varp = self.variance_population()
			result = varp ** (1 / 2)
		return result

	PAUTA_CRITERION = 0
	CHAUVENET_CRITERION = 1

	CHAUVENET_COEFFICIENT = {
		3: 1.38, 4: 1.53, 5: 1.65, 6: 1.75
		, 7: 1.80, 8: 1.86, 9: 1.92, 10: 1.96, 11: 2.0, 12: 2.03
		, 13: 2.07, 14: 2.10
	}

	def winkleGrossError(self, criterion, callbackStep):
		times = 0
		while len(self.m_data) > 2:
			noWinkled = True
			stddevs = self.std_dev_sample()
			mean = self.arithmetic_mean()
			c = 3 #if criterion == DataAnalysis.PAUTA_CRITERION else DataAnalysis.CHAUVENET_COEFFICIENT[len(self.m_data)]

			reserve = []
			winkled = []
			while self.m_data:
				num = self.m_data.pop()
				if abs(num - mean) > (c * stddevs):
					winkled.append(num)
					noWinkled = False
				else:
					reserve.append(num)
			self.m_data = reserve
			times += 1

			callbackStep(times, mean, stddevs, winkled, reserve)
			if noWinkled: break

if __name__ == '__main__':
	args = _CArgs(sys.argv)
	command = args.command()
	if command == 'winklegrosserror':
		#2017.11.2 Decide to use which algorithm. -p for Pauta criterion, -c for Chauvenet criterion(default)
		criterion = DataAnalysis.PAUTA_CRITERION if args.has_param('-p') else DataAnalysis.CHAUVENET_CRITERION
		data = [float(number) for number in sys.stdin.read().split()]

		def callbackStep(times, mean, stddevs, winkled, reserve):
			print("-----%d-----" % times)
			print("mean = %f, stddevs = %f" % (mean, stddevs))
			print("winkled = %s" % ' '.join([str(num) for num in winkled]))
			print("result = %s" % ' '.join([str(num) for num in reserve]))

		analyze = DataAnalysis(data)
		analyze.winkleGrossError(criterion, callbackStep)
		print("-----Final-----")
		print("mean = %f, stddevs = %f" % (analyze.arithmetic_mean(), analyze.std_dev_sample()))
		print("result = %s" % ' '.join([str(num) for num in analyze.data()]))
	elif command == 'uncertainty':
		data = [float(number) for number in sys.stdin.read().split()]
		analyze = DataAnalysis(data)

		mean = analyze.arithmetic_mean()
		stddevs = analyze.std_dev_sample()

		tP = 2.57
		A = tP * stddevs

		P = 0.95
		delta = 0.01
		B = P * delta

		U = (A ** 2 + B ** 2) ** (1 / 2)
		print("A: %f" % A)
		print("B: %f" % B)
		print("U: %f" % U)

	else:
		print('SuperLab cannot run the command: ' + command)