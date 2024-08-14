'''
x^2 + 2Ax + B = 0 조건을 만족하는 x 근 구하기
시간 제한 1초 => 1억번 계산
-1000 <= A,B <= 1000


1. 근 두개의 곱이 -1000 ~ 1000이라는 것, 근 두개의 합이 -2000 ~ 2000이하라는 것
=>x 의 범위를 -1000에서 1000정도면 다 나올 것 같음

2. 근의 공식
3. 근을 구하는 방식을 이용

'''

A,B = map(int,input().split())
result = []

for i in range(-1000,1001):
    if i*i + 2*A*i + B == 0:
        result.append(i)
    if len(result) >= 2:
        break

print(*result)
