'''
상근 -> 1<=B<=A<=500 두수를 고르낟
선영이는 상근이가 고른수를 맞춰야한다.

A제곱은 B제곱 보다 N만큼 크다
AB 쌍의 개수

1. 완전 탐색
A 500개, B 500개 => 25000개
A**2 = B**2 + N 을 만족하는지

2. A만 탐색 B가 범위에 있는지 확인

'''

N = int(input())

cnt = 0

for A in range(1,501):
    for B in range(1,501):
        if A**2 == B**2 + N:
            cnt += 1

print(cnt)