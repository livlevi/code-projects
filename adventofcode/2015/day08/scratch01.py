import re

string1 = ""
string2 = "abc"
string3 = "aaa\"aaa"
string4 = "\x27\x27"

pattern1 = r'\\[x]\d{2}'
pattern2 = r'\\\\'
pattern3 = r'\\"'
pattern4 = r'\\'
pattern5 = r'(\\x\d{2})|.'

matches = re.findall(pattern5, string4)
# r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

print(len(string4))
if matches:
    print(matches)
    print(len(matches))