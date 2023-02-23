#SWEA 문제 해결 기본 5118번 노드의 합
'''
리프 노드에 1000이하의 자연수
다른 노드에는 자식 노드에 저장된 값의 합이 들어있음
노드의 개수 N, 리프 노드의 개수 M, 출력할 노드 번호 L
리프 노드의 번호 L, 자연수를 준다

생각하는 풀이
N,M을 받는다
N으로 완전 이진 트리를 만든다.
리프 노드에 M을 넣는다.
후위 순회으로 앞 뒤에 것을 더해서 마지막 노드에 더하는 방식

'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    N,M,L = map(int, input().split())
    tree = [[0, 0, 0, 0] for _ in range(N + 1)]  # [왼쪽 자식, 오른쪽 자식, 부모 노드, 숫자] 각 인덱스는 자리를 의미
    for _ in range(M):
        leaf, num = map(int, input().split())
        tree[leaf][3] = num

    # tree 만들기
    for i in range(N, 0, -1):               # 합을 뒤에서부터 가져올 것이라서 뒤에서 부터 봐야한다.트리의 가지들을 하나씩 볼것

        # N을 넘어가면 자식 노드 제작 끝
        if (i*2 + 1) <= N:               # 자식 노드가 둘다 있는 경우
            tree[i][0] = i * 2           # 왼쪽 자식 노드
            tree[i][1] = i * 2 + 1       # 오른쪽 자식 노드
            tree[i][3] = tree[i * 2][3] + tree[i * 2 + 1][3]  # 그 자리에 들어가는 숫자

        elif (i*2) <= N:                 # 자식 노드가 하나만 있는 경우
            tree[i][0] = i * 2           # 왼쪽 자식 노드
            tree[i][3] = tree[i * 2][3]  # 그대로 올려줌

        tree[i][2] = i // 2          # 부모 노드의 값 = i // 2

    print(f'#{test_case}', tree[L][3])