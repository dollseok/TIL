#SWEA 문제해결 기본 4871번 그래프 경로

'''
V개의 노드, E개의 간선으로 연결한 방향성 그래프
특정한 두개의 노드에 경로가 존재하는지 확인하는 프로그램

테스트 케이스
첫번째 줄에 V, E
E개의 줄에 걸쳐 출발 도착 노드로 간선 정보
출발 노드 S, 도착 노드 G
'''

# 새로 푼 풀이(거의 유사)

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    V, E = map(int, input().split())    # V의 개수, E (길의 개수)
    arr = [[0]*V for _ in range(V)]
    visited = [False]*V
    stack = []
    res = 0

    # 방향성을 나타낸 arr 생성
    for i in range(E):
        v1, v2 = map(int, input().split())
        v1 = v1 - 1
        v2 = v2 - 1
        arr[v1][v2] = 1

    # for i in range(V):
    #     print(arr[i])

    S, G = map(int, input().split())
    S = S - 1
    G = G - 1

    v = S
    visited[v] = True

    while True:
        for w in range(V):
            if arr[v][w] == 1 and visited[w] == False:
                stack.append(v)
                v = w
                visited[w] = True
                break

        else:
            if not stack:              # 이어지는게 없을 경우
                res = 0                # 결과 = 0
                break
            v = stack.pop()            # 스택이 남아있으면 그리로 일단 돌아간다

        if v == G:                     # v가 goal에 도착했을 때
            res = 1                    # res = 1 갈수 있다는 것
            break

    print(f'#{test_case}', res)



#------------------------------------------------------------------------------------#
# 이전에 풀었던 풀이

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
