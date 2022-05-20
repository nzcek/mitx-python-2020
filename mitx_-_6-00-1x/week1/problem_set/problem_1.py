NumberOfVowels=0
v = "number of vowels: "

for letter in s:
if letter == 'a':
NumberOfVowels += 1
elif letter == 'e':
NumberOfVowels += 1
elif letter == 'i':
NumberOfVowels += 1
elif letter == 'o':
NumberOfVowels += 1
elif letter == 'u':
NumberOfVowels += 1
print(v + str(NumberOfVowels))
