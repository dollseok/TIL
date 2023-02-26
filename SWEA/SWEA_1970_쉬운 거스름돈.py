#SWEA 1970번 쉬운 거스름돈

'''
눂은 돈을 우선적으로 계산 할때 돈의 개수가 최소
50000, 10000, 5000, 1000, 500, 100, 50, 10

'''


import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    dict = { 50000 : 0, 10000 : 0, 5000 : 0, 1000 : 0, 500 : 0, 100 : 0, 50 : 0, 10 : 0}
    while N >= 10:
        if N >= 50000:
            div,rem = divmod(N,50000)   # 몫, 나머지
            dict[50000] += div
            N = rem
        elif N >= 10000:
            div, rem = divmod(N, 10000)   # 몫, 나머지
            dict[10000] += div
            N = rem
        elif N >= 5000:
            div, rem = divmod(N, 5000)   # 몫, 나머지
            dict[5000] += div
            N = rem
        elif N >= 1000:
            div, rem = divmod(N, 1000)   # 몫, 나머지
            dict[1000] += div
            N = rem
        elif N >= 500:
            div, rem = divmod(N, 500)   # 몫, 나머지
            dict[500] += div
            N = rem
        elif N >= 100:
            div, rem = divmod(N, 100)   # 몫, 나머지
            dict[100] += div
            N = rem
        elif N >= 50:
            div, rem = divmod(N, 50)   # 몫, 나머지
            dict[50] += div
            N = rem
        elif N >= 10:
            div, rem = divmod(N, 10)   # 몫, 나머지
            dict[10] += div
            N = rem


    print(f'#{test_case}')
    print(*dict.values())