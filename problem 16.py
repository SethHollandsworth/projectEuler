def powerdigitsum(n):
    n = n**1000
    items = []
    for i in str(n):
        items.append(int(i))

    return sum(items)

print(powerdigitsum(2))
    
        
