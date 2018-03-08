from primeChecker import primeChecker

def rotate(n):
	split = str(n)
	newSplit = split[1:] + split[0]
	return int(newSplit)

def isNotEven(n):
	if n == 2:
		return True
	split = str(n)
	nums = set(map(int, split))
	return all([n % 2 == 1 for n in nums])

def testRot(n):
	newN = n
	if not primeChecker(n):
		return False
	for i in range(len(str(n))-1):
		newN = rotate(newN)
		#print(newN)
		if not primeChecker(newN):
			return False
	return True


def circularPrimes(n):
	finalSet = set()
	for i in range(1,n + 1):
		if isNotEven(i) and testRot(i):
			finalSet.add(i)
			#print(i)
	return finalSet# + 13
n = 1000000
a = circularPrimes(n)
print(a)
print(len(a))
#print(circularPrimes(100000))
# print("PASS" if testRot(73) else "FAIL")
# print("PASS" if testRot(5) else "FAIL")
# print("PASS" if testRot(31) else "FAIL")
# print("PASS" if circularPrimes(100) == 13 else "FAIL")

