# viết chương trình nén chuỗi bằng cách đếm số lượng ký tự liên tiếp giống nhau.
# vd: AAABBB->3A3B. Lưu ý: cần phân biệt được chữ hoa, chữ thường, số và khoảng trắng.
def compress_string(s):
    if not s:
        return ""
    count = 1
    result = ""
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += str(count) + s[i-1]
            count = 1
    result += str(count) + s[-1]
    return result
s = input("s = ")
print(compress_string(s))