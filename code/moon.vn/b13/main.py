import os
path = ""
f_name = input()
path = os.path.join(path, f_name + ".txt")
print(path)