import re

ALPHA = "abcdefghijklmnopqrstuvwxyz"
I = "i"
O = "o"
L = "l"

passTests = False

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

def consecutiveChar(s):
    i = len(s) - 1
    while i >= 2:
        c = ord(s[i])
        b = ord(s[i - 1])
        a = ord(s[i - 2])
        if b == (c - 1) and a == (b - 1):
            return True  
        i -= 1
    return False

def noIOL(s):
    pattern = r'^(?:(?!i|o|l).)*$'
    return re.match(pattern, s)

def pairsLetters(s):
    for i in range(len(s) - 2):
        if s[i] == s[i+1]:
            j = i
            while j <= len(s) - 2:
                if s[j] == s[j+1] and s[i] != s[j] and s[i+1] != s[j+1]:
                    return True
                j += 1
    return False

originalpass = "cqjxxyzz"


# if pairsLetters(originalpass):
#     print("Found pars of characters.")
# else:
#     print("Haven't found pairs characters.")
count = 0
while not passTests:
    originalpass = nextpass(originalpass)
    print(originalpass)
    count += 1
    if consecutiveChar(originalpass) and noIOL(originalpass) and pairsLetters(originalpass):
        passTests = True

print(count)