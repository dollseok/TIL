T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    lst = list(map(int,input().split()))

    total_lst = [i for i in range(1,N+1)]

    not_submit_lst = []


    for k in total_lst:
        if k not in lst:
            not_submit_lst.append(k)

    print(f'#{tc}', *not_submit_lst)