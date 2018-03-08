def factors(n):
    return set(sum([[i, n//i] for i in range(1, int(n**.5)+1) if not n%i], []))




def reciprocalCycles(n):
	for i in range(10,n):
		denominatorFactors = factors(i)
		testForRepeating = sorted(list(set(denominatorFactors)))
		if testForRepeating != [2] or testForRepeating != [5] or testForRepeating != [2,5]:

			print(1/i)
		#if 2 in denominatorFactors
	return



print(reciprocalCycles(20))
#print(reciprocalCycles(1001))
