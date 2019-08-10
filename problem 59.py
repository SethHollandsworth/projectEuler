import string
f = open('p059_cipher.txt','r')
def helper(ch1, ch2):
    return chr((ch1)^(ord(ch2)))


letters = []
key = '.*z'
for line in f:
    letters = list(map(int,line.split(",")))
#letters = list(map(chr,(list(map(int,letters)))))

#print(letters)
#print(max(letters, key=letters.count))
#count = 0
# for i in string.ascii_lowercase:
#     print(i)
for n in range(0,len(letters),3):
    #print(n)
    try:
        print(helper(letters[n], key[0]), end='')
        print(helper(letters[n+1], key[1]) , end='')
        print(helper(letters[n+2], key[2]) , end='')
        
        # print(helper(letters[n], i), end='')
        # print(helper(letters[n+1], i) , end='')
        # print(helper(letters[n+2], i) , end='')
    except IndexError:
        print()
    #count +=3
        
#print(count)
#print(letters)