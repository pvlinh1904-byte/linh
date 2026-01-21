def findMinMax(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Tách các số nguyên (theo khoảng trắng và xuống dòng)
        numbers = list(map(int, content.split()))
        
        # Tìm min và max
        min_num = min(numbers)
        max_num = max(numbers)
        
        print(f"{max_num} {min_num}")
    
    except:
        print("Mission failed")
path = input().strip()
findMinMax(path)