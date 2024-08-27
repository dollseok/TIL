'''
imos를 이용해야하는 문제

1. 완전 탐색
매 입력마다 a,b 까지 모두 더해줘야함
100000 * 100000 정도의 시간 복잡도 나올 것으로 예상

2. imos
처음과 끝 k를 입력해줌

'''

n,m = map(int,input().split())

arr = [0] + list(map(int,input().split()))

imos = [0]*(n+2)

for _ in range(m):
    a,b,k = map(int,input().split())

    imos[a] += k
    imos[b+1] += -k

for i in range(1,n+2):
    imos[i] = imos[i-1] + imos[i]

for i in range(1,n+1):
    arr[i] += imos[i]

print(*arr[1:])