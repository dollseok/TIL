'''

1. 완전탐색
n 100000 ^ 2 => 2중 포문

2. 투포인터

'''

n = int(input())

ls = sorted(list(map(int,input().split())))

x = int(input())

s = 0
e = n - 1
cnt = 0
while s < e:
    tot = ls[s] + ls[e]
    if tot == x:
        cnt += 1

    if tot > x:
        e -= 1

    elif tot < x:
        s += 1
    else:
        s += 1
        e -= 1

print(cnt)


