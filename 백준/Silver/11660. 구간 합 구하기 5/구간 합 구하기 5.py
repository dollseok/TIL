'''
구간합 구하기 5

1초

N*N의 표 =>> N은 1024 이하
M 번의 구간합 구할것 -> 100000이하

x1,y1 => x2,y2까지 합을 구하는 프로그램

'''

N,M = map(int,input().split())
arr = [[0]*(N+1)]

for _ in range(N):
    arr.append([0] + list(map(int,input().split())))

prefix = [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        prefix[i][j] = arr[i][j] + prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1]

# for i in prefix:
#     print(i)

for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    print(prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1])
