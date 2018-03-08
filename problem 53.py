from math import *
def combinatoricSelections():
	finalList = []
	for n in range(1,101):
		for r in range(1,n):
			fact = factorial(n)/(factorial(r)*(factorial(n-r)))
			print(fact)
			if fact > 1000000:
				finalList.append(n)
	return len(finalList)

print(combinatoricSelections())
