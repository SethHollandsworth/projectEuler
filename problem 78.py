from primeChecker import primeChecker

def coinPartitions(n):
    vals = {1:1}
    for i in range(n):
        if i not in vals:
            vals[i] = 