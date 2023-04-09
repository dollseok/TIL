# BAEKJOON 10845번 큐

'''
정수를 저장하는 큐

push X : 정수 X를 큐에 넣음
pop : 큐에서 가장 위에 있는 정수를 빼고 그수를 출력 없으면 -1 출력
size : 큐에 들어있는 정수의 개수
empty : 큐이 비어있으면 1 아니면 0
front : 큐의 가장 앞에있는 정수를 출력, 없으면 -1
back : 큐의 가장 뒤에있는 정수를 출력, 없으면 -1
'''

import sys
input = sys.stdin.readline

N = int(input())
queue = []
front_num = 0

for _ in range(N):
    data = input().split()
    if data[0] == 'push':
        queue.append(data[1])
    elif data[0] == 'pop':
        if len(queue) != front_num:
            print(queue[front_num])
            front_num += 1
        else:
            print(-1)
    elif data[0] == 'size':
        print(len(queue)-front_num)
    elif data[0] == 'empty':
        if len(queue) != front_num:
            print(0)
        else:
            print(1)
    elif data[0] == 'front':
        if len(queue) != front_num:
            print(queue[front_num])
        else:
            print(-1)
    elif data[0] == 'back':
        if len(queue) != front_num:
            print(queue[-1])
        else:
            print(-1)