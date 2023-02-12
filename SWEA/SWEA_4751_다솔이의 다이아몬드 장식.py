#SWEA 4751번 다솔이의 다이아몬드 장식

'''
문자열 주변으로 장식을 추가해주는 문제
문자열이 두개 이상일 때 추가로 붙는것이 겹치는게 있는 문제

어느 부분에 어떤 순열로 인덱스에 들어간느지 알아내야하는게 포인트
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    word = list(input())
    n = len(word)
    line_length = 5 + 4 * (n-1)    # n개의 단어가 들어왔을 때, 각 line의 길이 # 첫번째만 다섯개 그 후로는 4개 열 씩 추가
    line1 = ['.']*line_length      # . 으로 모든 line을 채움
    line2 = ['.']*line_length
    line3 = ['.']*line_length
    line4 = ['.']*line_length
    line5 = ['.']*line_length

    # 수열을 고려해서 적정 위치에 교체를 해줌
    for i in range(line_length):
        if i % 4 == 2:            # #의 위치가 4n+2
            line1[i] = '#'
            line5[i] = '#'
            line3[i] = word[i//4] # 각 단어가 들어갈 위치
        if i % 2 == 1:            # 2,4번째 줄은 홀수 위치가 #
            line2[i] = '#'
            line4[i] = '#'
        if i % 4 == 0:            # 3번째 줄의 #의 위치는 4의 배수
            line3[i] = '#'

    print(''.join(line1))
    print(''.join(line2))
    print(''.join(line3))
    print(''.join(line4))
    print(''.join(line5))





