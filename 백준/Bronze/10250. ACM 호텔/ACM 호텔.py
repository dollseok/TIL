# SWEA 10250번 ACM호텔

'''
X가 작은 것 선호, 그다음 Y가 작은것 선호
'''

T = int(input())

for i in range(T):
    H,W,N = map(int,input().split())   # 6 12 12
    a = N//H + 1    # 2
    b = N % H   # 4

    if b == 0:
        b = H
        a -= 1

    if a < 10:
        res = str(b) + '0' + str(a)
    else:
        res = str(b) + str(a)

    print(res)