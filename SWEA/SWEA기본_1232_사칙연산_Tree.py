#SWEA 문제해결 기본 1232번 사칙 연산
'''
사칙 연산으로 구성되 이진트리
'''

import sys
sys.stdin = open("input.txt", "r")

def calc(o, a, b):
    if o == '-':
        return a - b
    elif o =='+':
        return a + b
    elif o == '*':
        return a*b
    elif o == '/':
        return a/b

for test_case in range(1,11):
    N = int(input())

    # 트리 제작
    tree = [0]       # [0,0,0,0] = [노드 인덱스, 정점 내용, 왼쪽 자식 노드, 오른쪽 자식 노드]
    data = [list(input().split()) for _ in range(N)]
    for d in data:
        if len(d) == 4:
            tree.append(d)
        elif len(d) == 3:
            tree.append(d + [0])
        elif len(d) == 2:
            tree.append(d + [0, 0])

    # print(tree)    # [0, ['1', '-', '2', '3'], ['2', '-', '4', '5'], ['3', '10', 0, 0], ['4', '88', 0, 0], ['5', '65', 0, 0]]

    # 뒤에서부터 계산식이 나오면 뽑아서 계산
    for i in range(N, 0, -1):
        if tree[i][1] in '+-*/':
            operator = tree[i][1]    # 연산자
            left = tree[int(tree[i][2])][1]
            right = tree[int(tree[i][3])][1]
            tree[i][1] = calc(operator, int(left), int(right))

    print(f'#{test_case}', int(tree[1][1]))