code = '111221'
final = []
i = 0

while i < len(code):
    if i == (len(code) - 1):
        final.append('1' + code[i])
    else:
        if code[i] == code[i + 1]:
            count = 1
            compare = code[i:]
            j = i  # Create a separate variable for iteration within the inner loop
            while j < len(compare) - 1 and code[j] == code[j + 1]:
                count += 1
                j += 1
            final.append(str(count) + code[i])
            i = j  # Update i to the last processed position
        else:
            final.append('1' + code[i])
    i += 1

print(final)
