'''
11047번 동전0

N개의 동전 종류 매우 많이 가지고 잇ㅇ므
합은 K로 만들려함. 동전 개수 최소값
'''

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
result = 0
coins = []

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

for i in range(n):
    if k >= coins[i]:
        result += k // coins[i]
        k = k % coins[i]

    if k == 0:
        print(result)
        break

