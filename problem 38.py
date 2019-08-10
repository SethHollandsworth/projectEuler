def isPandigital(n):
    pandigNums = set([1,2,3,4,5,6,7,8,9])
    separated = [int(i) for i in str(n)]
    for i in separated:
        if i in pandigNums:
            pandigNums.remove(i)
            #print(pandigNums)
    return len(pandigNums) == 0 and n > 10**8 and n < 10**9



def findPandigitals(n):
    allPandigs = set()
    for i in range(n):
        concatSums = ''
        j = 1
        while len(concatSums) < 9:
            concatSums += str(i * j)
            #print(concatSums)
            if len(str(concatSums)) == 9:
                if isPandigital(int(concatSums)):
                    allPandigs.add(int(concatSums))
                    #print(allPandigs)
            j += 1
    return max(allPandigs)






print(findPandigitals(1000000))


#print(isPandigital(143265789))
    