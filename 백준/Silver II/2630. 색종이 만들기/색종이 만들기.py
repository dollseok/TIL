'''
쿼드 트리
'''
n = int(input())
arr = []

result = [0,0]

for _ in range(n):
    arr.append(list(map(int,input().split())))

def quadTree(x,y,N):
    color = arr[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if color != arr[i][j]:
                quadTree(x,y,N//2)
                quadTree(x,y+N//2, N//2)
                quadTree(x+N//2, y, N//2)
                quadTree(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        result[color] += 1
    else:
        result[color] += 1

quadTree(0,0,n)

print(result[0])
print(result[1])