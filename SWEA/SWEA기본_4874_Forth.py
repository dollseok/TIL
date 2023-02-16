#SWEA 문제해결 기본 4874번 Forth

import sys
sys.stdin = open("input.txt", "r")

# 들어오는 i 가 문자열로 들어와서 계산을 해주는 함수를 만듦
def calc(a, b, i):
    if i == '+':
        return int(a) + int(b)
    elif i == '/':
        return int(a)//int(b)
    elif i == '-':
        return int(a) - int(b)
    elif i == '*':
        return int(a) * int(b)


T = int(input())
for test_case in range(1, T+1):
    N = input().split()
    # print(N)

    stack = []

    try:
        for i in N:
            if i == '.':                 # . 이 나왔을 때
                if len(stack) == 1:      # 한개가 마지막에 있다면
                    res = stack.pop()    # 정답 출력
                    break
                else:                    # 한개가 있지않고 여러개라면
                    res = 'error'        # 에러 발생   ( ex. 10 2 / 10 2 / . 이 경우에는 스택에 두개 남음)
                    break
            elif i.isdigit():                # 숫자라면
                stack.append(i)              # 스택에 바로 추가
            else:                            # 숫자가 아니라면
                B = stack.pop()              # 위에 먼저 꺼내고
                A = stack.pop()              # 다음것을 꺼내서
                stack.append(calc(A, B, i))  # 계산

    except:      # 오류가 나오면 에러
        res = 'error'

    print(f'#{test_case}', res)