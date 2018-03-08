"""figure out how to append the counts and starting numbers to the dictionary. the return value of count is not working"""
numbersAndSequenceLengths = [] 
finalList = []
count = 0
def collatzSequence(n):
	global count
	if n == 1:
		numbersAndSequenceLengths.append(count)
		count = 0
		return count
	elif n % 2 == 0:
		n = n/2
		count += 1
	else:
		n = 3*n + 1
		count +=1

	collatzSequence(n)

#def countingFunction(n):
#	count = 0
#	collatzSequence(n)



for i in range(1,1000000):
	numbersAndSequenceLengths.append(collatzSequence(i))

for item in numbersAndSequenceLengths:
	
	if type(item) == int:
		finalList.append(item)
print(max(finalList))




