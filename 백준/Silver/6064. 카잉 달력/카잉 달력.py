'''
6064번 카잉 달력

'''

t = int(input())
for _ in range(t):
    m,n,x,y = map(int,input().split())
    k = x
    result = -1
    while k <= m * n: # k의 범위는 m*n을 넘을 수 없다
        if (k-x) % m == 0 and (k-y) % n == 0: # 2개의 조건을 만족하는 k
            result = k
            break
        k += m # k-x가 m의 배수 -> k는 x로 초기화해주었기에 m만 더해줌 -> m을 더할 때마다 x값은 고정

    print(result)
