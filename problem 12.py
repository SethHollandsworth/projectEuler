from math import *
candidates = []

"""def highlyDivisibleTriangleNumber():
	a = 1
	for i in range(2,200000):
		a += i
		if a >= 62370000:
			candidates.append(a)"""
			
"""def highlyDivisibleTriangle2():
	for n in range(20000000):
		formula = n * (n + 1) / 2
		if len(str(formula)) >= 8 and type(formula) == int:
			candidates.append(formula)"""
		
"""def tests():
	for item in candidates:
		factors = []
		for j in range(1,item+1):
			if item %  == 0:
				factors.append(j)
		if len(factors) >= 500:
			return item"""
def numbers(length):
    for a in range(length):
        number = a*(a+1)/2
        if number >= 62370000:
            candidates.append(number)

def factors(n):    
    return len(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0))))
def final(listOfCandidates):
    for i in listOfCandidates:
        if factors(i) >= 500:
            return i
        

#highlyDivisibleTriangle2()
#print(candidates)
numbers(100000)
#print(candidates)
print(final(candidates))


