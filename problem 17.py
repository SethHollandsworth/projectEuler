def numberlettercounts():
	onesplace = {'1':3,'2':3,'3':5,'4':4,'5':4,'6':3,'7':5,'8':5,'9':4}
	tensplace = {'2':6, '3':6, '4':5, '5':5, '6':5, '7':7, '8':6, '9':6}
	counts = []
	for i in range(1,1000):
		i = str(i)
		if i[len(i)-1] != '0':
			counts.append(onesplace[i[len(i)-1]])
		if len(i) >= 2 and i[0] != '1':
			counts.append(tensplace[i[0]])
		return sum(counts)


print(numberlettercounts())













