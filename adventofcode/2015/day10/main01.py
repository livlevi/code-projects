code = '1321131112'
final = []
i = 0
loop = 0

while loop < 40:
    while i < len(code):
        if i == ( len(code) - 1 ):
            final.append('1' + code[i])
        else:
            if code[i] == code[i + 1]:
                count = 1
                compare = code[i:]
                j = 0
                while j < len(compare) and code[i] == code[i + 1]:
                    count += 1
                    i += 1
                    j += 1
                final.append(str(count) + code[i])
            else:
                final.append('1' + code[i])
        i += 1
    code = ''.join(final)
    loop += 1

print(loop)
print("This is length of final: ")
print(len(final))
print("This is length of code: ")
print(len(code))


