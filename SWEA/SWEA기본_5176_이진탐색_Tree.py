#SWEA 문제 해결 기본 5176번 이진탐색
'''
1-N까지의 자연수를 이진탐색 트리에 저장
이진탐색 트리의 특성을 이용해서 풀어보기
2**n 으로 커지는 개수 특성
'''

import sys
sys.stdin = open("input.txt", "r")

def inorder(node):
    global order
    if node != 0:
        # visit
        inorder(tree[node][0])
        order.append(node)
        inorder(tree[node][1])


T = int(input())
for test_case in range(1,T+1):
    N = int(input())                        # 정점의 개수
    tree = [[0,0,0] for i in range(N+1)]    # [왼쪽 자식 노드, 오른쪽 자식 노드, 부모 노드]
    name = 1
    order = [0]                             # 1-N까지 들어가는순서 & 인덱스 사용할거라 0을 넣어줌

    # 완전 이진 트리 제작
    for i in range(1, N+1):

        if tree[i][0] == 0:         # i의 왼쪽 자식 노드가 0이라면
            name += 1               # name 1 더함
            if name > N:            # name이 목표치를 넘으면 for문 끝냄
                break
            tree[i][0] = name       # tree에 왼쪽에 더함

        tree[name][2] = i           # 부모노드는 i

        if tree[i][1] == 0:         # i의 오른쪽 자식 노드가 0이라면
            name += 1               # name 1 더함
            if name > N:            # 목표치를 넘으면 for문 끝냄
                break
            tree[i][1] = name       # tree의 오른쪽에 이름 추가

        tree[name][2] = i           # 부모노드는 i

    inorder(1)
    # print(tree)
    # print(order)      # [0, 8, 4, 2, 5, 1, 6, 3, 7]

    # root는 order에서 1의 인덱스
    # order에서 N//2 = 4 의 인덱스가 원래 노드
    print(f'#{test_case}', order.index(1), order.index(N//2))