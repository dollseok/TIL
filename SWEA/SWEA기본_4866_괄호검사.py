#SWEA 문제해결 기본 4866번 괄호 검사

'''
괄호가 정상적으로 열고 닫혔는지 판별하는 문제
수혁님 코드 참고하기   #class
'''

# 새로 푼 풀이

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    code = input()
    n = len(code)
    stack = []
    res = 1

    for i in range(n):
        if code[i] in '(){}[]':    # 괄호인 경우만 체크
            if not stack:
                stack.append(code[i])
            else:
                if code[i] in '({[':          # 열리는 괄호면
                    stack.append(code[i])     # 스택에 추가
                else:                         # 열리는 괄호가 아닐 때
                    if code[i] == ')':
                        if stack[-1] == '(':  # 같은 쌍이면
                            stack.pop()       # 세트이니 스택에서 빼줌
                        else:                 # 같은 쌍이 아니면
                            res = 0           # 결과 0
                            break             # 검사 끝

                    elif code[i] == '}':
                        if stack[-1] == '{':
                            stack.pop()
                        else:
                            res = 0
                            break

                    elif code[i] == ']':
                        if stack[-1] == '[':
                            stack.pop()
                        else:
                            res = 0
                            break

    if stack:               # 다 끝나고 나왔는데 스택이 들어있으면
        res = 0             # 결과 0

    print(f'#{test_case}', res)






# -------------------------------------------------------------------------------#
# 이전에 풀었던 풀이


import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    sentence = input()
    stack = []
    res = 1

    for spell in sentence:
        if spell == '(' or spell == '{':     # 오픈되는 괄호가 들어왔을 때
            stack.append(spell)              # stack에 추가

        elif spell == ')' or spell == '}':   # 바로 닫힌 괄호가 들어왔을 때 = 오류
            res = 0                          # res = 0 하고 break
            break

        elif stack and spell == ')':         # stack이 차있고(빈 리스트가 아니고) 닫힌 괄호 ) 가 나왔을 떄
            if stack[-1] == '(':             # top 값 (가장 마지막 값)이 ( 로 쌍을 이룰 때
                stack.pop()                  # 그 값을 빼줌
            else:
                res = 0                      # 다른 괄호라면 오류
                break

        elif stack and spell == '}':         # stack이 차있고 닫힌 괄호 }가 나왔을 때
            if stack[-1] == '{':             # top 값이 {로 쌍을 이룰 때
                stack.pop()                  # 그 값을 빼줌
            else:
                res = 0                      # 다른 괄호라면 오류
                break

    if stack:                                # 스택이 차있다면 오류
        res = 0

    print(f'#{test_case} {res}')






# 내가 스택 제대로 이해 전에 풀었던 풀이
#
# T = int(input())
# for test_case in range(1, T+1):
#     top = -1
#     sen = list(input())       # 문장의 각 글자를 리스트로 받음
#     # print(sen)
#     res = 1                   # 결과값 옳게 되었으면 1, 아니면 0
#     stack = [0]*len(sen)      # stack을 sen(문장)의 길이만큼 만들어둠
#
#     # print('{} {}'.format(1, 2))  # input
#
#     for w in sen:
#         if w == '(' or w == '{':    # (, { 가 나온다면 스택에 추가하면서 top을 올리면서 w 추가
#             top += 1
#             stack[top] = w
#
#         if w == ')':                # ) 가 나왔을 때 앞에 (가 아니라면 오류
#             top -= 1
#             if stack[top+1] != '(':
#                 res = 0
#                 break               # 이미 오류이므로 break
#             else:
#                 stack[top+1] = 0    # ( 라면 원래 자리에 있던 것을 pop 해줌
#
#
#         if w == '}':
#             top -= 1
#             if stack[top+1] != '{':
#                 res = 0
#                 break
#             else:
#                 stack[top+1] = 0
#
#     # 만약에 (, ), {, } 가 스택에 남아있다면 res = 0 닫히지 않았으므로)
#     if '(' in stack:
#         res = 0
#     elif ')' in stack:
#         res = 0
#     elif '{' in stack:
#         res = 0
#     elif '}' in stack:
#         res = 0
#
#     print(f'#{test_case} {res}')
