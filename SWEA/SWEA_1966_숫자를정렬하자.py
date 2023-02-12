# SWEA 1966번 숫자를 정렬하자
'''
주어진 N 길이의 숫자열을 오름차순 정렬하는 문제
숫자열에는 0도 포함
텍스트 파일 안에 있는 최대값을 확인해서 공간 할당
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N개의 숫자

    lst = list(map(int, input().split()))  
    # print(lst)    # [15, 20, 8, 28, 16, 27, 17, 27, 10, 12]

    # counts : lst에 있는 숫자를 인덱스로 받아 몇개 들어있는지 확인하는 리스트
    # counts는 lst에 있는 숫자의 최대값으로 사이즈를 설정한다.

    size = 1   # 최소한 1개의 숫자는 있을 것이기에 size 변수로 설정
    for x in range(N):
        if (lst[x]) > size:
            size = (lst[x])
    counts = [0] * (size + 1)    # 0-N까지의 0을 포함한 사이즈여야함으로 size +1을 해줌
    # print(counts)     # counts = [0, 0, 0, 0, 0, ...0, 0]

    # counts의 요소를 채워줌(lst의 개수 세기)
    for x in lst:
        counts[x] += 1          # 각 숫자에 대한 counts의 idx자리에 카운트가 +1 씩 됨
    # print(counts)     #[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 1]
    for i in range(1, size + 1):
        counts[i] += counts[i-1]     # counts 누적합 리스트를 만듦, lst안에 있는 숫자가 몇번째로 들어갈지 알 수 있게 됨
    # print(counts)     #[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 9, 10]

    temp_lst = [0]*N    # lst와 사이즈가 같은 임시 리스트

    for i in range(N-1, -1, -1):    # lst를 역순으로 확인
        counts[lst[i]] -= 1
        # lst의 숫자가 counts의 idx로 표현되어있으니 count의 그 idx에 있는 숫자가
        # temp에서 정렬되었을때 몇번째 자리인지 나타내는 것
        temp_lst[counts[lst[i]]] = lst[i]    #temp의 위치에 lst 숫자를 넣음

    print(temp_lst)    #[8, 10, 12, 15, 16, 17, 20, 27, 27, 28]

    result = map(str, temp_lst)       # 각 숫자를 str로 바꾸어줌.
    res = ' '.join(result)
    print(f'#{tc} {res}')




