
N,L = map(int,input().split())

def solve():
    for k in range(L,101):
        min_sum = k * (k-1) // 2
        numerator = N - min_sum
        if numerator < 0:
            continue

        if numerator % k == 0:
            a = numerator // k
            seq = [str(a+i) for i in range(k)]
            print(" ".join(seq))
            return
    print(-1)

solve()