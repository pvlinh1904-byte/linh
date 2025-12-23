c = input("Nhập một chữ cái hoa: ")

if c == 'A':
    print("z")     # trường hợp đặc biệt
elif 'A' <= c <= 'Z':
    # chuyển sang chữ thường rồi trừ 1 ký tự
    lower_char = chr(ord(c) + 32)     # sang chữ thường
    previous_char = chr(ord(lower_char) - 1)
    print(previous_char)
else:
    print("Không phải chữ cái hoa!")
