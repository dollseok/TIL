import sys
input = sys.stdin.readline

T = int(input())

deq = []
for _ in range(T):
    command = input().strip()
    if command[-1].isdigit():
        content, x = command.split()
    else:
        content = command

    if content == "push_front":
        deq = [x] + deq
    elif content == "push_back":
        deq = deq + [x]
    elif content == "pop_front":
        if len(deq) > 0:
            print(deq[0])
            deq = deq[1:]
        else:
            print(-1)
    elif content == "pop_back":
        if len(deq) > 0:
            print(deq.pop())
        else:
            print(-1)
    elif content == "size":
        print(len(deq))
    elif content == "empty":
        if len(deq) > 0:
            print(0)
        else:
            print(1)
    elif content == "front":
        if len(deq) > 0:
            print(deq[0])

        else:
            print(-1)
    elif content == "back":
        if len(deq) > 0:
            print(deq[-1])
        else:
            print(-1)
