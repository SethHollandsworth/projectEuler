import primeChecker 

def truncate(dir,n):
	"""truncates a number from either left to right or right to left
	based on the input of dir. Dir goes left to right if it is true"""
	#print(n)
	if len(str(n)) == 1 and primeChecker.primeChecker(n):
		return True
	strnum = [int(i) for i in str(n)]
	if dir and primeChecker.primeChecker(n):
		return truncate(True,int(''.join(map(str,strnum[1:]))))
	elif not dir and primeChecker.primeChecker(n):
		#print(n)
		return truncate(False,int(''.join(map(str,strnum[:-1]))))
	else:
		return False

#print(truncate(True,7331))#==False)
#print(primeChecker.primeChecker(35))
