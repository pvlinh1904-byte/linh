def canWinNim(path):
    with open(path) as f:
        a = int(f.read().strip())
    return a % 4 != 0
print(canWinNim("linh.txt"))
