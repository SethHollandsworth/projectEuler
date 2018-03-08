def digitFifthPowers():
	finalList = []
	for i in range(0,10000000):
		yikes = []
		for letter in str(i):
			yikes.append(int(letter)**5)
			if sum(yikes) == i and len(yikes) == len(str(i)):
				finalList.append(i)
	return sum(finalList),finalList

print(digitFifthPowers())