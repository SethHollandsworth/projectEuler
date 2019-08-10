def d(n):
	factors = []
	for i in range(1,n):
		if n % i == 0:
			factors.append(i)
	return sum(factors)

def amicableNumbers():
	amicableNumberPairs = []
	for i in range(1,10001):
		a = d(i)
		b = d(a)
		if i == b and a != b:
			amicableNumberPairs.append(i)
			amicableNumberPairs.append(b)
	print(amicableNumberPairs)
	return sum(amicableNumberPairs)/2

print(amicableNumbers())

