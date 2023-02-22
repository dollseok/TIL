#SWEA 1861번 정사각형 방

'''
N**2개의 방이 NxN의 형태로 늘어서있다
상하좌우로 이동이 가능한데 숫자가 현재 방에서 정확히 1 커야한다

처음엔 부모노드 필요할 줄 알았는데 필요없음.
'''

import sys
sys.stdin = open("input.txt", "r")

di = [(1, 0), (0, 1), (-1, 0), (0, -1)]

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    # [[1, 2], [3, 4]]
    tree = [[0, 0, 0, 0] for _ in range(N**2+1)]     # 상 하 좌 우 연결되있는 것, 부모 노드

    # arr를 모든 요소를 보고 주변에 연결되있는 것을 확인하여 tree로 만든다
    for i in range(N):
        for j in range(N):
            for k in range(4):                                          # 4방향으로 연결되어있는것 확인
                if 0 <= i + di[k][0] < N and 0 <= j + di[k][1] < N:     # 범위 넘어가면 안봄
                    tree[arr[i][j]][k] = arr[i+di[k][0]][j + di[k][1]]  # arr[i][j] = 요소의 [k] 상하좌우에 있는 것을 tree에 넣는다
            # tree[arr[i+di[k][0]][j + di[k][1]]][4] = arr[i][j]        # 트리의 4번 인덱스에는 부모 노드를 넣는다 (필요없음)

    # print(tree)
    # [[0, 0, 0, 0], [3, 2, 0, 0], [4, 0, 0, 1], [0, 4, 1, 0], [0, 0, 2, 3]]
    # 0번 인덱스는 없는 것. 1번 인덱스 - 3, 2 연결되어있음. 2번 인덱스 - 4 1 연결되어있음 ...

    def postorder(node):                 # 후위순회로 이동한 칸 확인
        global cnt                       # cnt = 이동 칸 수
        cnt += 1                         # 함수 호출 될 때 cnt + 1
        if node != 0:                    # 노드가 0이 아니라면
            for k in range(4):           # 연결된 4개 확인
                if tree[node][k] == node + 1:     # 1만큼 딱 큰곳으로만 이동함으로 만약에 1을 더한 것이 같다면
                    postorder(tree[node][k])      # 이동한 위치에서 이어진 곳 있는지 확인

    res_list = [0]                      # 인덱스 사용할 거라 0 추가해둔 결과리스트
    for i in range(1, N**2+1):          # 모든 시작점들을 확인해서 가장 많은 cnt 결과 리스트에 넣음
        cnt = 0
        postorder(i)
        res_list.append(cnt)

    mx = 0
    res_index = 0
    for j in range(1, N**2 + 1):
        if mx < res_list[j]:
            mx = res_list[j]
            res_index = j

    print(f'#{test_case}', res_index, mx)


