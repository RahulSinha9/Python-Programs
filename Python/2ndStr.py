def count_substring(string, sub_string):
    a = 0
    for i in range (len(string)):
        if string.startswith(sub_string,i):
            a+= 1
    return a
