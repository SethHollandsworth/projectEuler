import math
def compareNums(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

file = open('p099_base_exp.txt','r')
baseExpPair = [0,0]
lineNum = 0;
bigNum = 0
for line in file:
	
    line = line.split(',')
    #print(line)
    lineNum += 1

    if int(line[1]) > baseExpPair[1] and int(line[0]) > baseExpPair[0]:
        print('num')
        val = int(math.log(int(line[1]),int(line[0])))
        print(val)
        if  val > bigNum:
            bigNum = val
            baseExpPair = [int(line[0]),int(line[1])]
		
		
            print(lineNum)


