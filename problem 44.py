pent = set([int(n*(3*n-1)/2) for n in range(1,10001)])
minNum =  float('inf')
for i in pent:
	for j in pent:
		if i + j in pent and j - i in pent:# and j - i < minNum:
			minNum = j - i





print(minNum)