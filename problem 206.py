def checksquare():
    for i in range(10**9,10**10,10):
        num = i**2
        num = str(num)
        strNum = num[::2]
        #print(i)
        if strNum == "1234567890":
            return i
        

print(checksquare())
#yo alex rodriquez
