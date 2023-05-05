import re

def my_title(string):
    return re.sub(
              r"[A-Za-z]+('[A-Za-z]+)?",
              lambda ch: ch.group(0)[0].upper() +
              ch.group(0)[1:].lower(),
              string
    )

text = input()
print(my_title(text))