#SWEA 문제해결 기본 1219번 길찾기

'''
graph로 하지말고 list로 만들어서 풀어보기 = 훨씬 시간 짧은
adjL[x].append(y)
용범님 코드 참고
'''

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

