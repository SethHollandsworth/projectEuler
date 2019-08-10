from math import *
def digitFactorials():
	finalList = []
	for i in range(3,100000):
		number = []
		for letter in str(i):
			number.append(factorial(int(letter)))
			if sum(number) == i:
				finalList.append(i)

	return sum(finalList)

print(digitFactorials())