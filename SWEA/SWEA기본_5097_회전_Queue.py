#SWEA 문제 해결 기본 5097번 회전

'''
원형큐 연습 문제
'''

# 원형큐로 연습한 풀이
n = 101
cQ = [0]*n
front = rear = -1

def isFull():           # q가 가득 차있는지?
    global rear
    return rear == n-1  # 차있다면 True

def isEmpty():          # q가 비었는지?
    global rear
    return front == rear

def enQueue(item):       # item 추가
    global rear
    if isFull():
        print("Queue_Full")
    else:
        rear = rear + 1
        cQ[rear] = item

def deQueue():           # 가장 앞에 것 빼줌
    global front
    if isEmpty():
        print("Queue_empty")
    else:
        front = front + 1
        return cQ[front]

T = int(input())
for tc in range(1,T+1):

    while not isEmpty():
        deQueue()               # 큐가 차있기 때문에 뒤에 답이 이상하게 나옴, 이전 값을 큐에서 비워줘야함.

    res = 0
    n, m = map(int, input().split())
    arr = list(map(int,input().split()))
    for a in arr:               # arr의 원소를 하나씩 가져옴
        enQueue(a)
    for _ in range(m % n):      # m번 만큼 반복하면 원상 복귀함 그래서 나머지만큼만 이동
        enQueue(deQueue())      # 맨앞의 것을 꺼내서 맨 뒤에 붙이는 것

    res = deQueue()

    print(f'#{tc}', res)






# 내 방식으로 그냥 푼 문제

import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    queue = input().split()

    # print(queue)

    for i in range(M):
        queue += [queue.pop(0)]

    print(f'#{test_case}', queue[0])




