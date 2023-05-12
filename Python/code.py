
roman_numerals = {"I" : 1,
                  "V" : 5,
                  "X" : 10,
                  "L" : 50,
                  "C" : 100,
                  "D" : 500,
                  "M" : 1000
                  }

int_value = 0

user_input = input("Enter Roman Number: ").upper()

for i in range(len(user_input)):
    if user_input[i] in roman_numerals:
            if i + 1 < len(user_input) and roman_numerals[user_input[i]] < roman_numerals[user_input[i + 1]]:
                int_value -= roman_numerals[user_input[i]]
            else:
                int_value += roman_numerals[user_input[i]]
            print("The integer value is: ", int_value)
    else:
        print("Invalid input.")