def champernowne2(n):
	constant = "0."
	for i in range(1,n+1):
		constant += str(i)
	print(int(constant[2])*int(constant[11])*int(constant[101])*int(constant[1001])*int(constant[10001])*int(constant[100001])*int(constant[1000001])) 

champernowne2(190000)