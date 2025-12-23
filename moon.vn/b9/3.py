s = input("s = ")

for i in range(0, len(s)):
    if (i % 2 == 0):
        print(s[i].lower(), end="")
    else:
        print(s[i].upper(), end="")
