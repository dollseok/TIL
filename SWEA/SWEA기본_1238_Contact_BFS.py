#SWEA 문제 해결 기본 1238번 contact

import sys
sys.stdin = open("input.txt", "r")

def bfs(adjL, start):            # 인접 리스트, start
    q = [start]                  # 초기 설정
    visited[start] = 1

    while q:
        v = q.pop(0)

        for i in adjL[v]:        # 연결되어있는 i들에 대해서
            if visited[i] == 0:  # 방문한 곳이 아니라면
                q.append(i)      # queue에 추가
                visited[i] = visited[v] + 1    # visited에 방문 인증



for test_case in range(1,11):
    N, S = map(int, input().split())    # N : 데이터의 길이, S : 시작점
    data = list(map(int,input().split()))
    adjL = [[] for _ in range(101)]     # (N은 최대 100이므로 101개로 해서 인덱스 사용할 것)인접 리스트   # 리스트 안 리스트는 for in range 사용
    visited = [0] * 101

    for i in range(N//2):
        v1, v2 = data[i*2], data[i*2 + 1]     # 데이터를 from to로 각각에 받아옴
        adjL[v1].append(v2)                   # v1에서 v2로 가는 것

    bfs(adjL, S)
    mx_idx = 100
    for i in range(100, -1, -1):               # 최대값 중에 최대 인덱스를 받을 것이기때문에 뒤에서부터 확인
        if visited[mx_idx] < visited[i]:
            mx_idx = i

    print(f'#{test_case}', mx_idx)
