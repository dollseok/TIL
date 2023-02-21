#SWEA 문제해결 기본 5102번 노드의 거리

'''
문제 설명 :
주어진 출발 정점에서 최소 몇개의 간선을 지나면 도착노드에 갈 수 있는지 알아내는 프로그램
ex) 1 - 4 - 6  : 2개
양방향 간선

2차원 배열을 사용해서 풀었음

인접 리스트를 이용한 풀이해보기
'''


import sys
sys.stdin = open("input.txt", "r")

def bfs(v, N):                  # v : 시작점, N = 도착점
    visited = [0]*(V+1)         # V의 개수만큼 visited 생성(0 인덱스는 안써서 V+1)
    q = [v]                     # queue에 v 시작점 추가해서 바로 queue 생성
    visited[v] = 1              # 시작점 visited 표시

    while q:                    # queue가 없을 때까지
        t = q.pop(0)            # dequeue
        for i in range(V+1):    # arr 인덱스를 뽑아야함으로
            if arr[t][i] == 1 and visited[i] == 0:    # t와 연결되어있는 i가 있고, i를 방문하지 않았었다면
                q.append(i)                           # q 에 i 추가
                visited[i] = visited[t] + 1           # 이전 깊이에서 다음 깊이으로 온것이므로 +1해서 visited 에저장

    # print(visited)
    # print(visited[N]-1)
    if visited[N] == 0:          # 연결되어있지 않으면 0이 나옴으로 0을 리턴
        return 0
    else:                        # 연결되어 있을 때 간선의 개수를 출력하는 것임으로 -1해서 리턴
        return visited[N] - 1    # 시작점으로부터 길이라고도 볼 수 있음.


T = int(input())
for test_case in range(1,T+1):
    V, E = map(int, input().split())          # V : 정점의 개수, E : 간선의 개수
    arr = [[0]*(V+1) for _ in range(V+1)]     # 0으로 가득찬 arr 제작 , 인덱스 0은 안쓸예정이라 V+1
    for _ in range(E):
        v1, v2 = map(int, input().split())    # 양방향 간선이라 연결되어있으면 대칭으로 추가
        arr[v1][v2] = 1
        arr[v2][v1] = 1

    S, G = map(int, input().split())          # S : start , G : goal

    # bfs(S,G)
    print(f'#{test_case}', bfs(S, G))
