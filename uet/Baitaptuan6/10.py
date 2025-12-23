L = list(map(int, input().split()))
k = int(input())
pairs = []
for i in range(len(L)):
    for j in range(i+1, len(L)):
        if L[i] + L[j] == k:
            pairs.append((L[i], L[j]))
pairs.sort(key=lambda x: x[0])
print(pairs)