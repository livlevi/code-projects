import re

re_d = re.compile(r'((\d)\2*)')
s = "1211"
match = re.search(r'((\d)\2*)', s)


if match:
    print("True")
else:
    print("False")
