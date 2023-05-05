#def square(num):
 #   return num**2
#
# square1 = square(10)
#print(square1)  
# def num(*number):
#     sum = 0
#     for i in number:
#         sum = sum + i
#     return sum    
# sum = num(1,2,3,3,4,5,65,65,8)
# print (sum)  
def fac(num):     
   n_fac = 1
   for i in range(1,num+1):
       n_fac = n_fac*i
   return n_fac
fac(5)             
    