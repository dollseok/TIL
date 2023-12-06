
T = int(input())

result = []

for _ in range(T):
    x,y = map(int,input().split())
    result.append([x,y])

result.sort()

for i in range(len(result)):
    print(*result[i])
