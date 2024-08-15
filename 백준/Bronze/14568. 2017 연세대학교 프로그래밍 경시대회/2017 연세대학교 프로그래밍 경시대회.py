'''
사탕 N 개
남는 사탕 x
남규는 영훈이보다 2개 이상 많은 사탕
셋 중 사탕 0개 없음
택희 받는 사탕은 홀수 x

규칙을 만족하는 세명에게 나누어주는 사탕 방법의 수
사탕은 총 100개

1.
A => 1 - 100개 남규
B => 1 - 100개 영훈
C => 1 - 100개 택희
각 조건 만족 확인



'''


N = int(input())
cnt = 0

for A in range(1,N):
    for B in range(1,N):
        for C in range(1,N):
            if A+B+C != N:
                continue
            if A < B+2:
                continue
            if C % 2 == 1:
                continue
            cnt += 1

print(cnt)