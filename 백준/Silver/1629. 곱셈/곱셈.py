'''
1629번 곱셈
분할 정복을 위한 거듭 제곱
'''

def fpow(a,n):
    if n == 1:
        return a%c
    else:
        x = fpow(a,n//2)
        if n%2 == 0:
            return (x*x)%c
        else:
            return (x*x*a) %c

a,b,c =map(int,input().split())
print(fpow(a,b))