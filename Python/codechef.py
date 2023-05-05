n = int(input())
for i in range(n):
	frnd, req = map(int, input().split())
    pizza = frnd*req//4
	if((frnd*req)%4==0):
    	print(pizza)
 else:
     
     
     
    	print(pizza+1)
	