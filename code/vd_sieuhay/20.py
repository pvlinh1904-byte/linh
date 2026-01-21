s = input()
do_dai = len(s) > 7
in_hoa = in_thuong = chu_so = False
for ch in s:
    if ch.islower():
        in_thuong = True
    elif ch.isupper():
        in_hoa = True
    else:
        chu_so = True
if do_dai and in_thuong and in_hoa and chu_so:
    print("Valid")
else:
    print("Invalid")