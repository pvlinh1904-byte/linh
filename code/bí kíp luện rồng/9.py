a = input().strip()
n = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
if a in alphabet:
    b = alphabet.index(a)
else:
    b = -1
c = (b + n) % 26
print(alphabet[c])