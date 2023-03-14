# 백준 2231번 분해합

'''
N이 주어졌을 때 N과 N을 이루는 각 자리수의 합을 분해합이라 한다

M의 분해합이 N인 경우 M을 N의 생성자라 한다
N이 주어졌을때 N의 가장 작은 생성자를 구하시오
없는 경우 0 출력
'''

# import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())

res = 0
for i in range(N):
    M = i + sum(map(int,list(str(i))))
    if M == N:
        res = i
        break

print(res)