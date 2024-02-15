n = int(input())
arr = []

result = [0,0]

for _ in range(n):
    arr.append(list(map(int,input().split())))

visited = [[False]*n for _ in range(n)]

origin_size = n
n = n*2
while n != 1:
    n = n//2
    checkpoint = []

    for i in range(origin_size//n):
        for j in range(origin_size//n):
            checkpoint.append((i*n,j*n))

    for x,y in checkpoint:
        pass_signal = False
        full_size = n * n
        start_num = arr[x][y]
        cnt = 0

        if not visited[x][y]:
            for i in range(n):
                for j in range(n):
                    tx = x + i
                    ty = y + j
                    if arr[tx][ty] != start_num:
                        pass_signal = True
                        break
                    else:
                        cnt += 1
                if pass_signal:
                    break

        # 한개가 전부 찼을 때
        if cnt == full_size:
            result[start_num] += 1
            # visited 변경
            for i in range(n):
                for j in range(n):
                    visited[x+i][y+j] = True

for i in result:
    print(i)
