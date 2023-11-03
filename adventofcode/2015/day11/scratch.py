import re

ALPHA = "abcdefghijklmnopqrstuvwxyz"

def nextpass(pw):
    if pw == '':
        return ''

    pw_list = list(pw)
    i = len(pw) - 1
    while i >= 0:
        index = ALPHA.index(pw_list[i]) + 1
        if index < len(ALPHA):
            pw_list[i] = ALPHA[index]
            break
        else:
            pw_list[i] = ALPHA[0]
            i -= 1

    return ''.join(pw_list)

def passRules(s):
    pattern1 = r'^[^iol]*$'
    pattern2 = r'.*?(\w)\1.*?(\w)\2'
    pattern3 = r'^(?:[a-wyz]{3}|[b-z]{3})$'
    return re.match(pattern2, s) and re.match(pattern1, s) and re.match(pattern3, s)

originalpass = "cqjxjnds"

for i in range(8):
    originalpass = nextpass(originalpass)
    print(originalpass)

# Validate the password against the rules
if passRules(originalpass):
    print("Password meets the rules.")
else:
    print("Password does not meet the rules.")
