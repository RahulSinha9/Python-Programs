# go ahead if you can optimise it...

def numinput():
	n=int(input("Number of lines 'only odd number' :: "))
	if (n%2!=0 and n>2):
		diode(n)
	else:
		print(":: Only odd numbers and not 1 ::")
		numinput()

print()

def diode(n):
	print()
	for i in range(1, n+3):
		for j in range(1, 5*(n+2)//2):
			if i<=n//2+2 and j<=i or i>1 and i<n+2 and j>=3*(n//2+2) or i>n//2+2 and j<=2*(n//2+2)-i:
				print("@",end="")
			elif i==n//2+2 and j>i and j<i*3:
				print("*",end="")
			else:
				print(" ",end="")
		print()
	print()
	numinput()

print()
print("It's a symbol like a diode.")
print()
numinput()