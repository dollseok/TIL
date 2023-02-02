# 4834번 숫자카드 만들기

import sys
sys.stdin = open("input.txt", "r")

def my_max(lst):
    max_num = 0
    for i in lst:
        if i > max_num:
            max_num = i
    return max_num


T = int(input())
for tc in range(1, T+1):
    N = int(input())        # 카드 장수    10
    a = list(str(input()))  # 숫자    7797946543
    # print(a)    # ['7', '7', '9', '7', '9', '4', '6', '5', '4', '3']
    count = [0] * 10
    for x in a:
        count[9-int(x)] += 1    # 애초에 index를 역으로 넣어줌.
        # int(x)가 9 라면 0번째자리
        # index함수를 썼을 때 가장 앞에 것이 나오기 때문에
    # print(count)  # [2, 0, 3, 1, 1, 2, 1, 0, 0, 0]
    max_num = my_max(count)

    print(f'#{tc} {9 - count.index(max_num)} {max_num}')
