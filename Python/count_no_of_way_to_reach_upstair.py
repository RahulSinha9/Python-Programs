def counts (n):
    if n <= 1:
        return n
    return counts(n-1) + counts(n-2)
def countNo(s):
    return counts(s+1)    
    
n = int(input())
result = countNo(n)
print(result)    