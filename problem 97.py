def nonMersennePrime():
	a = 28433
	b = 2**783.0457
	return str(a*(b**10000)+1)[-10:]

print(nonMersennePrime())

