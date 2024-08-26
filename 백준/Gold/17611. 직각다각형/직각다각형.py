'''
직각 다각형

imos 사용

ex) 세로만 보았을 때
각 좌표별로 1,-1을 양끝에 더해준다
current = 0,0
current , 3 / current = 3
1, current / current  = 1
current, 3  / current = 3
0, current / currrent = 0
current, 2 / current = 2
0 , current / current = 0

'''

n = int(input())

arr = []
maxW,minW,maxH,minH = -500001,500001,-500001,500001

for _ in range(n):
    x,y = map(int,input().split())
    maxW = max(x,maxW)
    minW = min(x,minW)
    maxH = max(y,maxH)
    minH = min(y,minH)
    arr.append([x,y])

arr.append(arr[0].copy()) # 그냥 넣으면 얕은 복사

for j in range(n+1):
    arr[j][0] -= minW
    arr[j][1] -= minH

imos_H = [0]*(maxH - minH + 1)
imos_W = [0]*(maxW - minW + 1)

current_x, current_y = arr[0]

for i in range(1,n+1):
    if arr[i-1][0] == arr[i][0]: # 세로 움직임
        target = sorted([arr[i][1],current_y])
        imos_H[target[0]] += 1
        imos_H[target[1]] += -1

        current_y = arr[i][1]

    else:
        target = sorted([arr[i][0],current_x])
        imos_W[target[0]] += 1
        imos_W[target[1]] += -1

        current_x = arr[i][0]

for i in range(1,maxW-minW+1):
    imos_W[i] = imos_W[i-1] + imos_W[i]

for j in range(1,maxH-minH+1):
    imos_H[j] = imos_H[j-1] + imos_H[j]

print(max(max(imos_W),max(imos_H)))