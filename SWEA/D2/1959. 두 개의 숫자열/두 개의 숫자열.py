T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())

    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    if N < M :
        small = N
        big = M
        small_list = A
        big_list = B
    else:
        small = M
        big = N
        small_list = B
        big_list = A

    max_sum = 0
    for j in range(big-small+1):
        sum_ = 0
        for i in range(small):
            sum_ += big_list[j+i]*small_list[i]

        if max_sum < sum_:
            max_sum = sum_

    print(f'#{tc}', max_sum)

