'''
N <= 300

N개 줄의 행렬

Q <= 100000
x1,y1 / x2,y2

이 범위 안에 있는 서로 다른 숫자

내가봣을 때 메모리는 좀 큰편

각 위치에 딕셔너리를 넣어줌 or list

prefix_dict => 그위치까지 누적합으로 개수가 몇개인지 확인
'''

N = int(input())

arr = [[0]*(N+1)]
for _ in range(N):
    arr.append([0] + list(map(int,input().split())))

prefix = [[[0]*11 for _ in range(N+1)] for _ in range(N+1)]


for i in range(1,N+1):
    for j in range(1,N+1):
        prefix[i][j][arr[i][j]] += 1
        for n in range(1,11):
            prefix[i][j][n] += prefix[i][j-1][n]
            prefix[i][j][n] += prefix[i-1][j][n]
            prefix[i][j][n] -= prefix[i-1][j-1][n]


Q = int(input())

for _ in range(Q):
    x1,y1,x2,y2 = map(int,input().split())

    answer = [0]*11
    for n in range(1,11):
        answer[n] = prefix[x2][y2][n] - prefix[x2][y1-1][n] - prefix[x1-1][y2][n] + prefix[x1-1][y1-1][n]

    print(11 - answer.count(0))
