def ngoac(s):
    stack = []
    matching = {
        ')': '(',
        '}': '{',
        ']': '['
}
    for i in s:
        if i in '({[':
            stack.append(i)
        elif i in ')}]':
            if not stack or stack[-1] != matching[i]:
                return "Invalid"
            stack.pop()
    if not stack:
        return "Valid"
    else:
        return "Invalid"
s = input()
print(ngoac(s))