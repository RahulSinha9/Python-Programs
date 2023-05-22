import string


print("Enter a String")
string = input()
all_freq = {}
for i in string:
    if i in all_freq:
        all_freq[i]  += 1
    else:
        all_freq[i]= 1
        print("count of all characters in string is:\n" + str(all_freq))