str1 = '1321131112'

for i in range(40):
    new = ''
    s = 0
    while s < len(str1):
        c = str1[s]
        n = 1
        s += 1
        while s < len(str1) and str1[s] == c:
            s += 1
            n += 1
        new += str(n) + str(c)
    str1 = new

print(len(str1))

str2 = str1

for i in range(10):
    new = ''
    s = 0
    while s < len(str2):
        c = str2[s]
        n = 1
        s += 1
        while s < len(str2) and str2[s] == c:
            s += 1
            n += 1
        new += str(n) + str(c)
    str2 = new

print(len(str2))
