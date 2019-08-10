def a3orA5():
    list1 = []
    for i in range(0,1000):
        if i %3==0 or i%5==0:
            list1.append(i)
    return sum(list1)
print(a3orA5())


def fibsum(n):
    sumList = [0,1]
    while sumList[len(sumList)-1]+ sumList[len(sumList)-2]<n:
        sumList.append(sumList[len(sumList)-1]+ sumList[len(sumList)-2])    
    list2 = sum([x for x in sumList if x%2==0])
    return list2
print(fibsum(4000000))

def primeFactorization(n):
    i = 2
    while i**2 <n:
        while n%i ==0:
            
            n=n/i
        i += 1
    return n
print(primeFactorization(600851475143))
        
def palindrome():
    listOfPalindromes = []
    smallerList = []
    for i in range(1000,100,-1):
        for x in range(1000,100,-1):
            num = str(i*x)
            if num == num[::-1]:
                listOfPalindromes.append(num)
    for item in listOfPalindromes:
        if len(str(item)) == 6:
            smallerList.append(item)
    return max(smallerList)
print(palindrome())

#def smallestMultiple():
#    count = 20
#    listOfStuff = []
#    for i in range(2520,1000000000):
#        if i%20==0 and i%19==0 and i%18==0 and i%17==0 and i%16==0 and i%15==0 and i%14==0 and i%13==0 and i%12==0 and i%11==0  and i%10==0 and i%9==0 and i%8==0 and i%7==0 and i%6==0 and i%5==0 and i%4==0 and i%3==0 and i%2==0:
#            listOfStuff.append(i)
#    return listOfStuff
#print(smallestMultiple())

def sumSquareDifference(n):
    each = 0
    for x in range(n):
        x = x**2
        each += x
    together = sum(range(n))**2
    return together - each
print(sumSquareDifference(101))
            

