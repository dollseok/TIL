#SWEA 문제해결 기본 4871번 그래프 경로

'''
V개의 노드, E개의 간선으로 연결한 방향성 그래프
특정한 두개의 노드에 경로가 존재하는지 확인하는 프로그램

테스트 케이스
첫번째 줄에 V, E
E개의 줄에 걸쳐 출발 도착 노드로 간선 정보
출발 노드 S, 도착 노드 G
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split()) # 노드 V는 1-V까지 사용
    visited = [False] * (V+1)        # 인덱스를 1부터 사용할 예정이여서 V+1로 index 0 을 안쓰고 하나 더 추가해줌
    stack = []
    graph = [[0] * (V+1) for _ in range(V+1)]    # 인덱스 이슈로 V+1로 추가

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a][b] = 1      # 단방향 노선
        # graph[b][a] = 1    # 사용하지 않아서 삭제

    # for i in range(V+1):
    #     print(graph[i])    # 그래프 확인

    S, G = map(int, input().split())     # S는 시작노드 G는 도착노드

    v = S            # v를 시작 노드로 잡아줌, S와 연결되었는지만 확인
    while True:      # 끝까지 도착할 때가지 반복
        for w in range(V+1):         # graph를 돌 것
            if graph[v][w] and not visited[w]:   # graph[v][w] = 1로 연결되있고 이전에 방문하지 않았다면
                stack.append(v)                  # stack에 v 추가해두고
                v = w                            # w로 이동
                visited[w] = True                # 방문 기록 남김
                break                            # 바로 다음 w로 옮겨진 v에서 확인
        else:                    # 위의 if문에 들어갈 수 없을 때 (이동위치에서 모두 탐색했을 때)
            if stack:            # 스택이 비지 않았다면
                v = stack.pop()  # 이전 단계로 돌아가게 v에 stack에서 pop해서 돌아가줌
            else:
                break

    if visited[G]:     # S - G가 연결되어서 True 라면
        res = 1
    else:
        res = 0

    print(f'#{test_case} {res}')
