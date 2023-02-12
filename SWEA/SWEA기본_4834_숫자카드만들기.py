# 4834번 숫자카드 만들기

'''
0-9까지 숫자가 적힌 N장의 카드
가장 많은 카드에 적힌 숫자와 카드가 몇장인지 출력하는 프로그램
'''

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
    a = list(input())       # 숫자    7797946543   #input이 애초에 str이라 str(input())에서 str 빼줌
    # print(a)              # ['7', '7', '9', '7', '9', '4', '6', '5', '4', '3']
    count = [0] * 10
    for x in a:
        count[9-int(x)] += 1    # 애초에 index를 역으로 넣어줌.
        # int(x)가 9 라면 0번째자리
        # index 함수를 썼을 때 가장 앞에 것이 나오기 때문에
    # print(count)  # [2, 0, 3, 1, 1, 2, 1, 0, 0, 0]
    max_num = my_max(count)

    print(f'#{tc} {9 - count.index(max_num)} {max_num}')
