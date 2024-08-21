'''
점수 따먹기

N*M의 행렬 , 각칸에 -10000  ~ 10000

부분행렬을 그려 그 안에 적힌 정수의 합을 구하는 게임
정수 합이 최대가 되는 부분행렬을 구하기

N 200 최대
M 200 최대

누적합 2차원

시작위치, 끝위치 경우의 수
200*200개 200*200개 => 1600000000 => 16억..

'''

n,m = map(int,input().split())

arr = [[0]*(m+1)]

for _ in range(n):
    arr.append([0] + list(map(int,input().split())))

# print(arr)
prefix = [[0]*(m+1) for _ in range(n+1)]

# 최대 40000번 계산
for i in range(1,n+1):
    for j in range(1,m+1):
        prefix[i][j] = arr[i][j] + prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1]

# for i in range(n+1):
#     print(prefix[i])

result = -100000000

for i in range(1,n+1):
    for j in range(1,m+1):
        # i,j 대상 지점 체크
        for k in range(1,i+1):
            for t in range(1,j+1):
                # k,t는 i-1과 j-1이 최대
                current = prefix[i][j] - prefix[k-1][j] - prefix[i][t-1] + prefix[k-1][t-1]
                # print(current, i,j, k,t)
                result = max(current,result)

print(result)




