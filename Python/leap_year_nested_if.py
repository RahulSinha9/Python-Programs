a = int(input("any year"))
if(a%100==0) and (a%400==0):
        print("leap year")
elif(a%4==0) and (a%100==0):
        print("leap year")
else:
        print("Not leap year")    
          #or
year = int(input("Enter any year\n"))
if(year%4==0):
    if (year%100==0):
        if (year%400==0):
            print("Leap year")
        else:
            print("Year in not leap year")     
        
    else:
        print("Leap year")      
        
else:
    print("year in not leap year")    
    