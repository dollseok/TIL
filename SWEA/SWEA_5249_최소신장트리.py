import sys
sys.stdin = open('input.txt','r')

# SWEA 5249번 최소 신장 트리

'''
그래프에서 사이클을 제거, 모든 노드를 포함하는 트리를 구성
가중치의 합이 최소가 되도록 만드는 최소 신장 트리라고 한다.

0~V까지의 노드, E개의 간선
'''

def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x,y):
    parent[find_set(y)] = find_set(x)


T = int(input())
for test_case in range(1,T+1):
    V,E = map(int,input().split())
    parent = [i for i in range(V+1)]
    graph = []
    for i in range(E):
        v1,v2,w = map(int,input().split())
        graph.append([w,v1,v2])

    graph.sort()
    # print(graph)

    N = V+1
    s = 0
    cnt = 0
    MST = []
    for w,u,v in graph:
        if find_set(u) != find_set(v):   # 같으면 이미 하나의 부모를 가지고 있는 것
            cnt += 1
            s += w
            MST.append([w,u,v])
            union(u,v)
            if cnt == N-1:
                break

    # print(MST)
    # print(parent)
    print(f'#{test_case}', s)