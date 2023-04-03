# SWEA 5248 그룹나누기

'''
참여하고 싶은 사람끼리 두사람의 출석번호 종이에 적어 제출
연결되면 모두가 한조
1-N의 출석 번호, M장의 신청서
전체 몇개의 조가 만들어질까
'''

def dfs(start):

    visited[start] = 1          # 지나간 곳은 방문 표시
    while lst[start]:           # 그 노드의 리스트가 빌 때까지 확인
        dfs(lst[start].pop())   # 다음 dfs 진행


T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    data = list(map(int,input().split()))
    lst = [[] for _ in range(N+1)]
    visited = [0]*(N+1)

    for i in range(len(data)//2):            # 양방향으로 추가해줘서 연결된 것을 확인
        lst[data[2*i]].append(data[2*i+1])
        lst[data[2*i+1]].append(data[2*i])

    cnt = 0
    for i in range(1,N+1):
        if visited[i] == 0:
            if lst[i] != 0:      # 어딘가와 연결되어있으면
                dfs(i)           # dfs로 어디까지 가는지 탐색
            cnt += 1             # 연결되어있지 않거나, dfs로 탐색하고 나오면 개수 + 1

    print(f'#{test_case}', cnt)