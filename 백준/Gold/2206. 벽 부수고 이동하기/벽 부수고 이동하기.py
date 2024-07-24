'''
벽 부수고 이동하기
n x m 의 행렬
1,1 -> n,m의 최단 경로

풀이
dfs로 풀어야한다
dfs 최단 경로 다음 단계로 갈 때
1일 때
부수거나 안부수거나
부순적이 있는지 없는지까지 체크 => 단 한번만 부수기 가능

0일 때
dfs 평소처럼 진행

틀림 -> bfs 로 수정

최종 풀이
distance 를 총 두층으로 나눠서 3차원 배열
0층 => 부수기 전 거리 데이터
1층 => 부수고 난 후 거리 데이터

두 거리의 데이터를 같이 저장
가장 먼저 도착하면 return 해서 bfs 끝냄
다 끝났는데 도착을 못하면 return -1

'''

from collections import deque

n,m = map(int,input().split())

arr = [list(map(int,list(input()))) for _ in range(n)]
distance = [[[0]*2 for _ in range(m)] for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y):
    q = deque()
    q.append([y,x,0])
    distance[y][x][0] = 1

    while q:
        y,x,break_cnt = q.popleft()

        if (x,y) ==(m-1,n-1):
            return distance[y][x][break_cnt]

        for i in range(4):
            ty,tx = y + dy[i], x+dx[i]
            if 0 <= ty< n and 0 <= tx < m:

                if arr[ty][tx] == 1 and break_cnt == 0:
                    distance[ty][tx][1] = distance[y][x][0] + 1
                    q.append([ty,tx,1])
                elif arr[ty][tx] == 0 and distance[ty][tx][break_cnt] == 0:
                    distance[ty][tx][break_cnt] = distance[y][x][break_cnt] + 1
                    q.append([ty,tx,break_cnt])

    return -1

print(bfs(0,0))
