# SWEA 1966번 숫자를 정렬하자
'''
텍스트 파일 안에 있는 최대값을 확인해서 공간 할당
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if N < 5 or N > 50:    # 범위 초과 예외 처리
        print('N 범위를 초과했습니다.')

    lst = list(map(int, input().split()))

    # counts 의 사이즈 설정
    size = 1
    for x in range(N):
        if (lst[x]) > size:
            size = (lst[x])
    counts = [0] * (size + 1)    # 0-N까지의 사이즈여야함으로 size +1을 해줌
    # print(counts)     # counts = [0, 0, 0, 0, 0, ...0, 0]

    # counts의 요소를 채워줌(lst의 개수 세기)
    for x in lst:
        counts[x] += 1          # 각 숫자에 대한 counts의 idx자리에 카운트가 +1 씩 됨
    # print(counts)     #[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 1]
    for x in range(1, size + 1):
        counts[x] += counts[x-1]     # counts 리스트 변경, 앞에 것을 더해서 각 자리를 찾아갈 것
    # print(counts)     #[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 9, 10]

    temp = [0]*N    # 각 숫자를 오름차순으로 정렬해줄 temp 설정

    for i in range(N-1, -1, -1):    # lst를 역순으로 확인
        counts[lst[i]] -= 1
        # lst의 숫자가 counts의 idx로 표현되어있으니 count의 그 idx에 있는 숫자가
        # temp에서 정렬되었을때 몇번째 자리인지 나타내는 것
        temp[counts[lst[i]]] = lst[i]    #temp의 위치에 lst 숫자를 넣음

    print(temp)    #[8, 10, 12, 15, 16, 17, 20, 27, 27, 28]

    result = map(str, temp)       # 각 숫자를 str로 바꾸어줌.
    res = ' '.join(result)
    print(f'#{tc} {res}')




