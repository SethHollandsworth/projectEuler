def distinctPowers():
	col = []
	for a in range(2,101):
		for b in range(2,101):
			col.append(a**b)
	return len(list(set(col)))


print(distinctPowers())

