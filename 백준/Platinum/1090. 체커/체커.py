N = int(input())
l = []
INF = 10e9
result = [INF]*N
result[0] = 0
xset = set()
yset = set()

for i in range(N):
    x, y = map(int,input().split())
    l.append((x,y))
    xset.add(x)
    yset.add(y)

candidate = []
for i in xset:
    for j in yset:
        candidate.append((i,j))

for cx,cy in candidate:
    distance = [0]*N
    for i in range(N):
        distance[i] = abs(cx-l[i][0]) + abs(cy-l[i][1])

    distance.sort()
    for i in range(1,N):
        distance[i] = distance[i] + distance[i-1]
        result[i] = min(distance[i], result[i])

print(*result)