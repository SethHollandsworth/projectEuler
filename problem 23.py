from math import *
deficientNumbers = []
perfectNumbers = []
abundantNumbers = []
finalList = []
def factors(n):    
    return (set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0))))


def makeListOfPerfectNumbers():
        for i in range(1,28123):
                #print(sum(factors(i)))
                #if sum(factors(i)) < i:
                #       deficientNumbers.append(i)
                #if sum(factors(i)) == i:
                #       perfectNumbers.append(i)
                if sum(factors(i)) > i:
                       abundantNumbers.append(i)
                       



def nonAbundantSums():
        for i in range(28123):
                for number in abundantNumbers:
                       if (i - number) not in abundantNumbers and i not in abundantNumbers:
                               finalList.append(i)


makeListOfPerfectNumbers()
print(abundantNumbers)
