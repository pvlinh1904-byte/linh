s = input()
result = ""
prev_space = True
for ch in s:
    if ch != ' ':
        result += ch
        prev_space = False
    else:
        if not prev_space:
            result += ' '
            prev_space = True
if result and result[-1] == ' ':
    result = result[:-1]
print(result)