#SWEA 문제해결 기본 1217번 계산기 3

import sys
sys.stdin = open("input.txt", "r")

def isp(i):
    if i == '+' or i == '-':
        return 1
    if i == '*' or i == '/':
        return 2
    if i =='(':
        return 0

def icp(i):
    if i == '+' or i == '-':
        return 1
    if i == '*' or i == '/':
        return 2
    if i =='(':
        return 3

for test_case in range(1,11):
    N = int(input())
    st = input()

    prefix = []
    stack = []

    # print(st)
    for i in st:
        if i.isdigit():
            prefix.append(i)

        else:
            if i == ')':
                while stack[-1] != '(':
                    k = stack.pop()
                    prefix.append(k)
                stack.pop()

            else:
                if not stack: # 스택이 비었다면
                    stack.append(i)

                else:                                    # 스택이 들어있다면
                    if isp(stack[-1]) < icp(i):          # 스택에 들어있는게 클 때
                        stack.append(i)
                    else:                                # 들어오는 것이 스택보다 작을 때
                        while isp(stack[-1]) >= icp(i):   # 스택에 있는 것이 작아질 때까지 pop해서 prefix에 추가
                            k = stack.pop()
                            prefix.append(k)
                        stack.append(i)

    # print(prefix)

    # 후입 표기법 계산하기

    for i in prefix:

        if i.isdigit():
            stack.append(i)

        else:
            B = stack.pop()
            A = stack.pop()
            if i == '+':
                stack.append(int(A)+int(B))
            elif i == '-':
                stack.append(int(A) - int(B))
            elif i == '*':
                stack.append(int(A) * int(B))
            elif i == '/':
                stack.append(int(A) / int(B))

    ans = stack.pop()
    print(f'#{test_case}', ans)

