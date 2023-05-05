a = ['A','B','C','D','E','F','G']
# print(a)
#, print(a[0]),
 
# print(type(a))
# print(type(a[0]))
# print(a[2:5])
# print(a[2:])
# print(a[ :5])
# print(a[-5:-2])
# print(a[-6:-2])
# print (a[5:0:-1]);print (a[0:7:-1]);print (a[-1:-6:-1])
# a.reverse()
# a.sort()
# print(list(range(10)))
# print(list(range(10,10,3)))
# print(list(range(-10,-100,-30)))
# b = list(range(10))
# b.reverse()
# print(b)
a = ['Delhi','Noida','Lucknow','Goa']
a[2] = "Bihar"
print(a)
a.append("Patna")
print(a)
mylist = list("Bihar")
print(mylist)
l1 = list("ABC")
l2 = list("XYZ")
l3 = l1+l2
print(l3)
l3.remove('Z')
print(l3)
# l3.remove('P')
# print(l3)
if 'P' in l3:
    l3.remove('P')
    print("P remove from l3")
else:
    print("P not present in l3")
    
alpha  = input()
if alpha in l3:
    l3.remove(alpha) 
    print(alpha)
else:
    print(alpha)
    

             