from math import *
def pythagtrip():
    odds = []
    
    for i in range(1,500,2):
        for j in range(1,499):
            for k in range(1,498):
                print(i,j,k)
                if i**2 + j**2 == k**2 and i+j+k==1000:
                    return i*j*k
#print(pythagtrip())
    
def pythagtrip2():
    emptyList = []
    for i in range(1,500):
        for j in range(1,499):
            k =i**2 + j**2
            
            print (i,j,int(k**.5),int(k**.5)+i+j)
            if (k**.5 + i + j) == 1000:
                emptyList.append(i*j*int(k**.5))
    return emptyList

def pythagtrip3():
    emptyList = []
    for i in range(1,500):
        for j in range(1,499):
            k =i**2 + j**2

            if int(floor(k**(.5))) + int(i) + int(j) == 1000:
                emptyList.append(i)
                emptyList.append(j)
                emptyList.append(k**.5)

    return emptyList

print(pythagtrip2())
