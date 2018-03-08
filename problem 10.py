
def primes(n):
	prime = []
	for p in range(2, n+1):
		for i in range(2, p):
			if p % i == 0:
				break
			else:
				prime.append(p)

	return sum(prime)

def primes_sieve1(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return sum([i for i in primes if primes[i]==True])

print (primes_sieve1(2000000))
#print(primes(2000000))
