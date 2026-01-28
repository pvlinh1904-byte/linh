def housesOfHogwarts(path):
    with open(path, "r") as f:
        ten = f.readlines()
    for i in ten[1:]:
        print(i.strip())
housesOfHogwarts("linh.txt")
