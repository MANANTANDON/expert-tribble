strings = ["flower", "flow", "flight"] 
lowerNumber = len(strings[0])
prefix = ""

for word in strings:
    if len(word) < lowerNumber:
        lowerNumber = len(word)

for i in range(lowerNumber):
    char = strings[0][i]

    for j in range(len(strings)):
        if char != strings[j][i]:
            print(prefix)
            exit()

    prefix += char

print(prefix)
