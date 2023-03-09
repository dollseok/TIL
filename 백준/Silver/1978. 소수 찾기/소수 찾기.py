# 백준 1978번 소수 찾기

'''
주어진 수 N개 중에서 소수가 몇개인지 찾아서 출력하는 프로그램
'''

# import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())
data = list(map(int,input().split()))

decimal = [1]*1001

for i in range(2,1000):
    for j in range(2,1000):
        if i*j > 1000:
            break
        decimal[i*j] = 0

cnt = 0
for i in data:
    if i != 1 and decimal[i] == 1:
        cnt += 1

print(cnt)
