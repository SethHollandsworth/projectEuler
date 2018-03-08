
def selfPowersno48():
	finalList = []
	for i in range(1,1001):
		finalList.append(i**i)
	return sum(finalList)
print(selfPowersno48())
