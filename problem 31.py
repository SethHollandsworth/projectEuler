penny = 1
doublePenny = 2
nickel = 5
dime = 10
doubleDime = 20
halfPound = 50
pound = 100
doublePound = 200

def coinSums(S,m,n):
	#we need n+1 rows in the table
	table = [[0 for j in range(m)] for i in range(n+1)]
	for i in range(m):
		table[0][i] = 1
	for i in range(1,n+1):
		for j in range(m):
			x = table[i - S[j]][j] if i-S[j] >= 0 else 0
			y = table[i][j-1] if j >= 1 else 0
			print(x,y)
			#total count
			table[i][j] = x + y

	return  table[n][m-1]

arr = [penny,doublePenny,nickel,dime,doubleDime,halfPound,pound,doublePound]
m = len(arr)
n = 200

print(coinSums(arr,m,n))