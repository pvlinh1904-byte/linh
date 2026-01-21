def compress_string(s):
    if not s:
        return ""
    result = ""
    count = 1
    current = s[0]
    for i in range(1, len(s)):
        if s[i] == current:
            count += 1
        else:
            result += str(count) + current
            current = s[i]
            count = 1
    result += str(count) + current
    return result
s = input()
print(compress_string(s))