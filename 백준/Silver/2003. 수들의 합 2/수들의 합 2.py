'''
수들의 합 2

i~j까지 범위의 합을 구하는 것

1. 완전 탐색
i,j 다 잡아서 2중 포문

2. 누적합

3. 투포인터

'''

n,m = map(int,input().split())
ls = list(map(int,input().split()))

s = 0
e = 0

tot = ls[s]
cnt = 0

while e < n and s < n:
    # print(tot,s,e)
    if e != n-1:
        if tot < m:
            e += 1
            tot += ls[e]
        elif tot > m:
            tot -= ls[s]
            s += 1
        else:
            cnt += 1
            tot -= ls[s]
            s += 1
            e += 1
            tot += ls[e]
    else:
        if tot > m:
            tot -= ls[s]
            s += 1
        elif tot == m:
            cnt += 1
            tot -= ls[s]
            s += 1
        else:
            break

print(cnt)

'''
3 1
1 2 1

5 2
5 2 1000 1 1

1 1
1

'''