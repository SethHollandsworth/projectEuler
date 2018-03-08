from primeChecker import primeChecker
from itertools import permutations
from itertools import combinations

def isPerm(n,check):
	check = set(map(int, set(str(check))))
	n = set(map(int, set(str(n))))
	for i in n:
		if i in check:
			check.remove(i)
	return len(check) == 0

def findPerms(n):
	return set(map(int,list(map("".join, permutations(str(n))))))

def diff(arr):
	diffs = []
	nums = []
	for i in range(len(arr)):
		for j in range(i,len(arr)):
			diffs.append(arr[j] - arr[i])
			if arr[j] - arr[i] in diffs:
				nums.append(arr[i])
				nums.append(arr[j])
	return nums

def primePerms():
	allPossible = []
	#idx = 0
	for i in range(1000,10000):
		allPerms = findPerms(i)
		count = 0
		numsInSeries = []
		for j in allPerms:
			if primeChecker(j) and j > 1000:
				count += 1
				numsInSeries.append(j)
		if count >= 3 and sorted(numsInSeries) not in allPossible:

			allPossible.append(sorted(numsInSeries))
			#idx += 1
	return allPossible

def getPatterns():
	allNums = primePerms()
	#print(allNums)
	for series in allNums:
		series = list(combinations(series, 3))
		#print(series)
		
		for k in series:
			diffs = [j-i for i, j in zip(k[:-1], k[1:])]
			#print(diffs)
			if (diffs[0] == diffs[1]):
				print(k)
				print(diffs)

#print(diff([2843, 4283, 8243]))
#print(primePerms())
getPatterns()
#print(final)
		

	
