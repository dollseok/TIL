#SWEA 문제해결 기본 1225번 암호생성기

'''
8개의 숫자를 입력 받음
첫번째 숫자를 1 감소시킨 뒤, 맨 뒤로 보냄
다음 첫번째 숫자를 2 감소시킨 뒤 맨뒤로, 그 다음에 다시 첫번째 수를 3 감소시킨 뒤 맨뒤로 그다음 4 그다음 5
이렇게 한 사이클

숫자가 감소할 때 0보다 작아지는 경우 0 으로 유지되고 프로그램 종료
'''


import sys
sys.stdin = open("input.txt", "r")

def isFull():           # Queue가 가득 차있는지?
    global rear                       # rear를 더하고 빼고하기 때문에 global로 부름
    return (rear+1) % (N+1) == front  # 차있다면 True

def isEmpty():          # Queue가 비었는지?
    global rear                       #
    return front == rear              # front = rear면 Queue가 비어있는 것

def enQueue(item):       # item 추가
    global rear
    if isFull():                      # Queue가 가득찼다면
        print("Queue_Full")           # 더 들어가지 못함 - Queue 다찼음을 알려줌
    else:
        rear = (rear + 1) % (N+1)     # 시작하면 rear가 8일텐데,
        Q[rear] = item                # 바로 다음 0부터 해서 채움

def deQueue():           # 가장 앞에 것 빼줌
    global front                      #
    if isEmpty():                     # Queue가 비었다면
        print("Queue_empty")          # 나올 것이 없음 - Queue가 비었음을 알려줌
    else:
        front = (front + 1) % (N+1)   # front를 하나 밀어주고
        return Q[front]               # front에 있던 것을 리턴


for _ in range(1):
    test_case = int(input())
    password = list(map(int, input().split()))
    N = 8              # 8자리의 비밀번호
    Q = [0]*(N+1)      # Queue를 원형큐이기 때문에 front를 비워두면서 다음 저장소를 하나 만들어둬야해서

    # 기본 세팅
    mn = 999999
    for i in password:

        if mn > i:
            mn = i

    b = mn//15                                  # 15로 나눈 몫 , 사이클이 8번 돌면 모두 같은 값이 빠지고 원상 복귀, 그때 빠지는 값이 15
    for i in range(8):
        password[i] = password[i] - (b-1)*15    # 15로 나누어 떨어지는 경우에는 0이 되버린다. - 0이면 안됨으로 b-1로 계산

    # print(password)               # [25, 31, 25, 28, 33, 26, 26, 26]   # 여기부터 시작

    # 원형큐 사용해서 품
    front = rear = 0
    for i in password:              # [0, 25, 31, 25, 28, 33, 26, 26, 26]   # rear는 1에서부터 더 해지기 시작
        enQueue(i)

    # print(Q)                      # [0, 25, 31, 25, 28, 33, 26, 26, 26]
    cnt = 0                         # 최종 Q에서 위치를 확인하기 위한 cnt
    while True:
        for i in range(1, 6):       # 1-5 까지 싸이클 반복
            cnt += 1                # 한번 과정 거칠 때 cnt + 1
            temp = deQueue() - i       # Queue의 가장 앞 부분을 빼서 임시 변수 temp에 넣어줌
            if temp <= 0:              # temp가 0보다 작거나 같으면
                temp = 0               # temp를 0으로 고정
                enQueue(temp)          # Queue에 temp를 추가
                break                  # 0 이 나왔으면 break (여기는 for문 break)
            else:                      # 0 이하가 안나왔다면
                enQueue(temp)          # temp 그대로 Queue에 추가

        if Q[(cnt - 1) % 9] == 0:      # while문 브레이크 조건 : 마지막 부분이 0 이라면 끝냄
            break

    # front,rear가 0-9까지 왔다갔다해서 마지막 결과 도출 조건을 걸어줌
    # front + 1인 이유는 front부분은 이미 빠졌기 때문
    if front > rear:                        # front가 rear보다 뒤에 있을 때
        res = (Q[front+1:] + Q[:rear+1])    # front 바로 뒤에부터 끝까지 & 처음부터 rear까지
    else:                                   # front가 rear보다 앞에 있을 때
        res = Q[front + 1 : rear + 1]       # front 바로 뒤에부터, rear까지

    print(f'#{test_case}', *res)






