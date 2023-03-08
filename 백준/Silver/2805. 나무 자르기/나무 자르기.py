# 백준 2805번 나무 자르기

'''

'''

# import sys
# sys.stdin = open('input.txt', 'r')

N, M = map(int,input().split())
trees = list(map(int, input().split()))

mn_H = 0
mx_H = max(trees)
sum_ = 0
res = []

while True:
    mid = (mx_H+mn_H)//2
    for i in trees:
        if i >= mid:
            sum_ += i - mid

    if sum_ == M:
        res = mid
        break

    if sum_ > M:
        if mid in res:
            res = max(res)
            break
        res.append(mid)
        mn_H = mid
        sum_ = 0

    else:
        if mid in res:
            res = max(res)
            break
        mx_H = mid
        sum_ = 0

print(res)