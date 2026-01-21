s = input()
s = s.lower()
count = {}
for ch in s:
    if ch != " ":
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
for ch in count:
    print(ch, ":", count[ch])