#SWEA 문제해결기본 5177번 이진힙
'''
최소힙
마지막 노드 뒤에 새 노드를 추가
부모 노드의 값 < 자식 노드의 값
노드의 번호는 완전 이진 트리를 따른다

구할 것
입력 순서대로 최소힙에 저장하고 마지막 노드의 조상 노드에 저장된 정수의 합

입력
T 테스트 케이스의 개수
N개의 자연수
서로 다른 N개의 자연수 데이터

풀이
트리를 만든 후에
이진 탐색을 통해 하나씩 res에 값을 넣고 sum을 사용해서 모두 합한다.
'''

'''
주석 예시 input
6
7 2 5 3 4 6
'''


import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = map(int, input().split())

    tree = [[0, 0, 0, 0] for _ in range(N+1)]    # [왼쪽 노드, 오른쪽 노드, 부모 노드, 숫자] 각 인덱스는 이진트리에서 인덱스

    # 빈 완전 이진 트리 제작
    for i in range(1, N+1):
        if i*2 + 1 <= N:                 # 오른쪽 노드가 있으면
            tree[i][0] = 2 * i           # 왼쪽 노드 추가
            tree[i][1] = 2 * i + 1       # 오른쪽 노드 추가
        elif i*2 <= N:                   # 왼쪽 노드만 있으면
            tree[i][0] = 2 * i           # 왼쪽 노드 추가

        tree[i][2] = i // 2              # 부모 노드 추가

    # print(tree)    # [[0, 0, 0, 0], [2, 3, 0, 0], [4, 5, 1, 0], [6, 0, 1, 0], [0, 0, 2, 0], [0, 0, 2, 0], [0, 0, 3, 0]]

    # 최소힙 만들어 주기

    i = 0
    for d in data:            # 데이터를 하나씩 넣어줄 것
        i += 1
        if tree[i][3] == 0:   # 빈칸이라면 넣어줌
            tree[i][3] = d
            tmp = i           # 임시 변수
            while tmp != 0:   # tmp 꼭대기까지 확인
                if tree[tmp//2][3] < tree[tmp][3]:   # 부모의 값이 현재 값보다 작으면 끝
                    break
                else:                                # 부모의 값이 현재 값보다 크면 바꿔주고
                    tree[tmp//2][3], tree[tmp][3] = tree[tmp][3], tree[tmp//2][3]
                    tmp = tmp // 2                   # 바꾼 부모의 값도 그것의 부모와 확인 반복

    # print(tree)    # [[0, 0, 0, 0], [2, 3, 0, 2], [4, 5, 1, 3], [6, 0, 1, 5], [0, 0, 2, 7], [0, 0, 2, 4], [0, 0, 3, 6]]

    # 조상 노드까지 올라가기

    tmp = tree[N][2]                        # 마지막 노드의 부모노드
    res_list = []                           # 조상 노드들을 모아줄 리스트
    while tmp != 0:                         # tmp = 0이면 더 올라갈 부모 노드가 없다는 것
        res_list.append(tree[tmp][3])       # 결과리스트에 부모 노드의 값을 추가
        tmp = tmp // 2                      # 부모 노드의 부모 노드 확인

    # print(res_list)   # [5, 2]

    print(f'#{test_case}', sum(res_list))


# # 수업 시간 풀이
# def enq(n):    # 최소 이진힙
#     global last
#     last += 1              # last 자리를 한자리 늘려줌
#     tree[last] = n         # tree의 마지막 자리에 n을 넣어줌
#     c = last               # child는 last고
#     p = c // 2             # parent는 c//2 이다
#
#     while p > 0 and (tree[p] > tree[c]):         # parent 0이하로 갈수도 있어서 방지, 부모 노드가 자식 노드보다 더 크다면
#         tree[p], tree[c] = tree[c], tree[p]   # 자리 바꿈
#         c = p                                 # 반복해서 다시 확인인
#         p = c // 2
#
# def get_sum(tree):
#     p_node = N // 2
#     p_sum = 0
#     while tree[p_node]:
#         p_sum += tree[p_node]
#         p_node = p_node // 2
#     return p_sum
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     data = list(map(int,input().split()))
#     tree = [0] * (N+1)
#     last = 0
#     for a in data:
#         enq(a)
#
#     res = get_sum(tree)
#
#     print(f'#{tc}', res)

