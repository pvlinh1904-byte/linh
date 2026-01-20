text = input()
vowels = 0
consonants = 0
vowels_set = "aeiou"
for ch in text:
    if ch.isalpha():
        ch = ch.lower()
        if ch in vowels_set:
            vowels += 1
        else:
            consonants += 1
print(vowels)
print(consonants)