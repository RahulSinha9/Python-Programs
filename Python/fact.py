def fac(num):     
    n_fac = 1
    for i in range(1, num+1):
       n_fac = n_fac * i
    return n_fac
d = fac(int(input()))
print(d)
