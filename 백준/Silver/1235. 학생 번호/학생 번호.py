n = int(input())
data = [list(map(int,input().strip())) for _ in range(n)]

length = len(data[0])
for i in range(length-1, -1, -1):
    tmp = [[] for _ in range(n)]
    setData = set()
    for j in range(n):
        tmp[j].append(data[j][i:])
        setData.add(str(tmp[j]))
    if len(setData)==n:
        print(length-i)
        break
