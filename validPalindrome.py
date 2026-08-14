# Leet Code: STRINGS
# Valid Palindrome


# import re

# s = "A man, a plan, a canal: Panama"
# s = "race a car"

# removeChars = re.sub('[^A-Za-z0-9]+', '', s.lower())

# if (removeChars == removeChars[::-1]):
#     print(True)
# else:
#     print(False)



#without the import function
s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s=" "
removeChars = ""

for chars in s.lower():
    if chars.isalnum():
        removeChars += chars

if(removeChars == removeChars[::-1]):
    print(True)
else:
    print(False)

