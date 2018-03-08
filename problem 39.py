def integerRightTriangles():
	pull = []
	for perimeter in range(1,1001):
		count = 0
		for i in range(1,500):
			for j in range(1,500):
				if i + j + (i**2 + j**2)**.5 == float(perimeter):
					count+=1
		if count >8:
			pull.append([perimeter,count])
	return pull

print(integerRightTriangles())