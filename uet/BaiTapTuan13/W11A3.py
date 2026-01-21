def housesOfHogwarts(path: str):
    with open(path, 'r') as f:
        lines = f.readlines()
    
    # Dòng đầu là số lượng tên, bỏ qua
    for name in lines[1:]:
        print(name.strip())
housesOfHogwarts("hogwarts.txt")
