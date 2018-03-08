# import truncate
from primeChecker import *

def truncRightLeft(n):
	strNum = str(n)
	while (len(strNum)) >= 1:
		#print(strNum)
		if not primeChecker(int(strNum)):
			return False
		strNum = strNum[:-1]
	return True


def truncLeftRight(n):
	strNum = str(n)
	while (len(strNum)) >= 1:
		if not primeChecker(int(strNum)):
			return False
		strNum = strNum[1:]
	return True

def isNotEven(n):
	if n == 2:
		return True
	split = str(n)
	nums = set(map(int, split))
	return all([n % 2 == 1 for n in nums])

def truncPrimes(maxNum):
	summed = 0
	count = 0
	for i in range(10, maxNum):
		if ( truncLeftRight(i) and truncRightLeft(i)):
			summed += i
			count += 1
			print(i)
	print(count)
	return summed


print(truncPrimes(1000000))
