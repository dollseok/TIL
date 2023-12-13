"""
N! 에서 뒤에서부터 처음 0 이 아닌 숫자가 나올떄까지의 0의 개수
"""

import sys
input = sys.stdin.readline

N = int(input())
factorial = 1
for i in range(1,N+1):
    factorial = factorial*i

factorial = str(factorial)
l = len(factorial)

cnt=0
for i in range(l):
    if factorial[l-1-i] == '0':
        cnt += 1
    else:
        break

print(cnt)
