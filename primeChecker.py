#import time
import math
def primeChecker(n):
	if n == 1:
		return False
	if n == 2:
		return True
	for i in range(2,math.ceil(n**0.5) + 1):
		#print(i)
		if n % i == 0:
			return False
	return True





#print(primeChecker(3))






#start = time.time()
#print(primeChecker(1009))
#end = time.time()
#print(end-start)