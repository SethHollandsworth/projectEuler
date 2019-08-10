def doubleBasePalindromes():
	finalList = []
	for i in range(1,1000000):
		if str(i) == str(i)[::-1]:
			if str(format(i,'b')) == str(format(i,'b'))[::-1]:
				finalList.append(i)
	return sum(finalList)


print(doubleBasePalindromes())
