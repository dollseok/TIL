#SWEA 문제해결 기본 1234번 비밀번호

'''
붙어있는 쌍 소거하고 남은 번호를 비밀번호로 만드는 문제
소거된 번호 쌍 좌우 번호가 같은 번호이면 또 소거 가능
'''

import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    N, password = input().split()
    stack = []
    for spell in list(password):
        if not stack:
            stack.append(spell)
        else:
            if spell != stack[-1]:    # 스택의 가장 마지막과 spell이 다르면
                stack.append(spell)   # stack에 추가
            elif spell == stack[-1]:  # 스택의 가장 마지막과 spell이 같으면
                stack.pop()           # stack 마지막 pop

    print(f'#{test_case}', ''.join(stack))




# for test_case in range(1, 11):
#     N, password = input().split()
#     stack = [0]*int(N)
#     top = -1
#     # print(list(password))
#     for spell in list(password):        # 비밀번호를 문자열로 하나씩 받음
#         if spell != stack[top]:         # 현재 탑과 다르다면
#             top += 1                    # 탑을 하나 올리고
#             stack[top] = spell          # 탑에 글자 추가
#         elif spell == stack[top]:       # 현재 탑과 같다면
#             top -= 1                    # 스택에서 빼줌
#
#     print(f'#{test_case}', ''.join(stack[:top+1]))
