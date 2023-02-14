#SWEA 문제해결 기본 4873번 반복문자 지우기

# 수혁님 코드 읽어보기 - class 사용
# append, pop을 사용하는게 스택이다
# 현재 내가 푼 방법은 카운트 한 것

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    sentence = list(input())
    stack = [0] * len(sentence)      # 문장 길이 만큼의 stack 미리 생성
    top = -1                         # top을 0부터 시작
    # print(sentence)

    for spell in sentence:
        if spell != stack[top]:      # 현재 탑과 비교했을 때 다르면
            top += 1                 # 탑 위치 하나 올리고
            stack[top] = spell       # 탑 위치에 글자 넣음
            # top += 1

        elif spell == stack[top]:    # 현재 탑과 같다면
            top -= 1                 # 현재 탑을 스택에서 뺀다
            # stack[top] = 0         # 필요 없어서 삭제, 어차피 top으로 스택은 결정됨

    print(f'#{test_case} {top+1}')    # 탑은 인덱스이므로 문자열의 길이는 top + 1
