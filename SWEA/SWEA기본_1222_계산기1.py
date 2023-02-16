# SWEA 문제 해결 기본 1222번 계산기 1

import sys
sys.stdin = open("input.txt", "r")


for test_case in range(1, 11):
    # 후위 표기식 만들기
    N = int(input())
    a = list(input())
    # print(a)

    stack = []
    res = []

    for tok in a:
        if tok.isdigit():
            res.append(tok)
        else:
            stack.append(tok)

    while stack:
        res.append(stack.pop())

    # print(res)

    # 후위 표기식 계산하기
    calc_stack = []

    for i in res:
        if i.isdigit():
            calc_stack.append(i)
        else:
            B = calc_stack.pop()
            A = calc_stack.pop()
            calc_stack.append(int(A)+int(B))

    calc_res = calc_stack.pop()
    print(f'#{test_case}', calc_res)
