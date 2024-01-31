import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())

for t in range(T):
    # 데이터 입력받기
    p = list(input().strip()) # 커멘드 리스트
    n = int(input()) # 숫자 개수
    arr = input().strip()
    num_list = deque(arr[1:-1].split(","))
    if n == 0:
        num_list = deque()

    # 진행 방향
    reverse = False# 1이면 앞쪽 -1 이면 뒤쪽
    result = True

    if p == [] and 'D' in num_list:
        result = False

    for function in p:
        if function == 'R':
            reverse = not reverse
        elif function == 'D':
            if num_list:
                if reverse:
                    num_list.pop()
                else:
                    num_list.popleft()
            else:
                result = False

    if not result:
        print('error')
    else:
        if reverse:
            num_list.reverse()
            print("[" + ",".join(num_list) + "]")
        else:
            print("[" + ",".join(num_list) + "]")

