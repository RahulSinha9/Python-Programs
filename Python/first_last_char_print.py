print("Enter a string")
string = input()
FirstAndLast = string
def FirstAndLast(string):
    for i in range(len(string)):
        if i == 0:
            print(string[i],end = "")
        if i == len(string) - 1:
            print(string[i],end ="")    
        if string[i] ==" ":
            print(string[i-1],string[i+1],end = "") 
        else:
            print("null")       