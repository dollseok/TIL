
# BAEKJOON 10828번 스택

'''
정수를 저장하는 스택

push X : 정수 X를 스택에 넣음
pop : 스택에서 가장 위에 있는 정수를 빼고 그수를 출력 없으면 -1 출력
size : 스택에 들어있는 정수의 개수
empty : 스택이 비어있음녀 1 아니면 0
top : 스택의 가장 위에있는 정수를 출력, 없으면 -1
'''

import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    data = input().split()
    if data[0] == 'push':
        stack.append(data[1])
    elif data[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif data[0] == 'size':
        print(len(stack))
    elif data[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif data[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)