# Leet Code: STRINGS
# Roman to Integer

roman = "III" #"LVIII" #"MCMXCIV"
values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "0": 0 }

i = 0
finalValue = 0

while i < len(roman):
    a = roman[i]
    b = "0" if i == len(roman) - 1 else roman[i + 1]

    if values[a] >= values[b]:
        finalValue += values[a]
        i += 1
    else:
        finalValue += values[b] - values[a]
        i += 2

print(finalValue)