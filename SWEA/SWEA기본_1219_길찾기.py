#SWEA 문제해결 기본 1219번 길찾기

'''
DFS 문제 - 다시 돌아오는 것 고려하지 않고 만듦.

graph로 하지말고 list로 만들어서 풀어보기 = 훨씬 시간 짧은
adjL[x].append(y)
용범님 코드 참고
'''

# 다시 푼 풀이

import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    test_case, N = map(int,input().split())
    visited = [False]*100     # 0-99의 visited
    arr = [[0]*100 for _ in range(100)]
    # print(arr)

    in_lst = list(map(int, input().split()))       # 0 1 0 2 1 4 1 3 4 8 4 3 2 9 2 5 5 6 5 7 7 99 7 9 9 8 9 10 6 10 3 7
    for i in range(N):
        v1, v2 = in_lst[i*2], in_lst[i*2 + 1]
        arr[v1][v2] = 1                            # 이동경로 하나씩 arr에 저장

    stack = []     # 서칭했을 때 없을 때 돌아갈 i를 저장해둠
    i = 0          # 시작은 0

    while True:
        for j in range(100):
            if arr[i][j] == 1 and visited[j] == False:
                stack.append(i)
                i = j
                visited[j] = True
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break

    if visited[99]:
        res = 1
    else:
        res = 0


    print(f'#{test_case}', res)


# ------------------------------------------------------------------------------------------#
# 첫번째로 풀었던 풀이

import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    test_case, E = map(int, input().split())
    way_list = list(map(int, input().split()))
    graph = [[0] * 100 for _ in range(100)]  # 끝 도착지점이 99
    visited = [False] * 100
    stack = []
    for i in range(E):
        v = way_list[2*i]       # 출발 노드
        w = way_list[2*i + 1]   # 도착 노드
        graph[v][w] = 1      # v와 w를 연결

    v = 0
    while True:
        for w in range(100):
            if graph[v][w] and not visited[w]:
                stack.append(v)
                v = w
                visited[w] = True
                break

        else:
            if stack:
                v = stack.pop()
            else:
                break

    if visited[99]:
        res = 1
    else:
        res = 0

    print(f'#{test_case} {res}')

