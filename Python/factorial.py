 #import math
from math import factorial

print("Enter any number")
fac = int(input())
#print(math.factorial(fac))
factorial = 1
if fac< 0:
    print("Sorry, factorial does not exixt for negative numbers")
elif fac == 0:
    print("Factorial of 0 is 1")
else:
   for i in range (1,fac + 1):
   print("The factorial of number is ",fac,factorial) 
          
 
 
