final = 0
for i in range(101):
	for j in range(101):
		bigNum = sum([int(d) for d in str(i**j)])
		if bigNum > final:
			final = bigNum

print(final)