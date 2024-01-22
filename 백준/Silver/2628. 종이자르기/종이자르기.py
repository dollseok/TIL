n, m = map(int,input().split()) # 가로 세로

arr = [[0]*n for _ in range(m)]

width = [0,n]
length = [0,m]

cut = int(input())
for _ in range(cut):
    line = list(map(int,input().split()))
    if line[0] == 0:
        length.append(line[1])
    else:
        width.append(line[1])

width.sort()
length.sort()
result = 0

for i in range(len(width) - 1):
    for j in range(len(length) - 1):
        w = width[i+1] - width[i]
        l = length[j+1] - length[j]
        result = max(result, w*l)

print(result)