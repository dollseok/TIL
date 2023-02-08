#SWEA 5432번 쇠막대기 자르기

'''
끝점은 겹치지 않는다
짧은 막대기는 긴 막대기 위에 있다

() 모양이 레이저

'''

import sys
sys.stdin = open("input.txt", "r")

# 길이를 확인하는 함수
def my_len(a):
    cnt = 0
    for _ in list(a):
        cnt += 1
    return cnt

T = int(input())
for test_case in range(1, T+1):
    background = input() + '0'      # 전체를 받아옴, 아래 if문에서 하나 더 검사해야해서 오류안나게 '0' 추가
    N = my_len(background) - 1      # 길이가 하나 더 길어졌으므로 -1
    i = 0                           # 시작점
    current_stick = 0               # 현재 막대 수
    total_stick = 0                 # 총 막대 수

    while i != N:      # i가 N일 때 까지 확인을 할 것임
        # 레이저 인지 확인
        if background[i] + background[i+1] == '()':
            i = i+2                      # 레이저라면 인덱스 2 넘김
            total_stick += current_stick

        # 레이저가 아니라면
        else:
            if background[i] == '(':     # (, 스틱의 시작점, 현재 스틱 개수 추가
                current_stick += 1
                i += 1

            elif background[i] == ')':   # ), 스틱의 끝점, 현재 스틱 개수 하나 빼면서 총 개수 추가
                current_stick -= 1
                total_stick += 1
                i += 1

    print(f'#{test_case}', total_stick)





