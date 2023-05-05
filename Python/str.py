S=input()
a=0
for i in range(len(S)):
    if S[i].isalnum():
         a+=1
if a>0:
    print ('True')
else:
    print ('False')

a=0
for i in range(len(S)):
    if S[i].isalpha():
         a+=1
if a>0:
    print ('True')
else:
    print ('False')
    
a=0
for i in range(len(S)):
    if S[i].isdigit():
         a+=1
if a>0:
    print ('True')
else:
    print ('False')
    
a=0
for i in range(len(S)):
    if S[i].islower():
         a+=1
if a>0:
    print ('True')
else:
    print ('False')
    
a=0
for i in range(len(S)):
    if S[i].isupper():
         a+=1
if a>0:
    print ('True')
else:
    print ('False')