'''
중복 순열
전체 개수! // 중복 개수 !
'''

t = int(input())

dp = [0]*(11)

def factorial(n):
    if n == 0:
        return 1
    else:
        fac = 1
        for i in range(1,n+1):
            fac = fac * i
        return fac

lst = []
for _ in range(t):
    result = 0
    n = int(input())
    for i in range((n//3)+1): # 3이 쓰인 개수
        tmp = n-i*3 # 3이 들어가고 남은 수
        for j in range((tmp//2)+1):
            rest = n - (i * 3) - (j * 2) # 남은 1의 개수
            # i : 3의 개수, j : 2의 개수, rest: 1의 개수
            result += factorial(rest+i+j) // (factorial(i) * factorial(j) * factorial(rest))

    print(result)