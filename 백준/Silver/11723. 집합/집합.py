'''
11723번 집합
'''
import sys
input = sys.stdin.readline

m = int(input())
s = [False]*21

for _ in range(m):
    data = list(input().split())
    if data[0] == 'add':
        s[int(data[1])] = True
    elif data[0] == 'remove':
        s[int(data[1])] = False
    elif data[0] == 'check':
        if s[int(data[1])]:
            print(1)
        else:
            print(0)
    elif data[0] == 'toggle':
        s[int(data[1])] = not s[int(data[1])]
    elif data[0] == 'all':
        s = [True]*21
    elif data[0] == 'empty':
        s = [False]*21

