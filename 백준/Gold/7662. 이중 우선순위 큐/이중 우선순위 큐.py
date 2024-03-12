'''
7662번 이중 우선순위 큐

연산 개수 k <= 1000000
I n : n을 Q에 삽입하는 연산
D 1 : Q에서 최대값 삭제
D -1 : Q에서 최솟값 삭제

6초 -> 1000000 * log (1000000) 가 최악의 경우 충분 -> heapq
'''

import sys
import heapq

input = sys.stdin.readline


t = int(input())

for _ in range(t):
    k = int(input())
    min_hq = []
    max_hq = []
    exist = [True]*k # exist가 True면 있는 것
    for idx in range(k):
        cal, num = input().split()
        num = int(num)
        if cal == 'I':
            heapq.heappush(min_hq,(num,idx))
            heapq.heappush(max_hq,(num*-1,idx))
        else:
            if num == -1: # 최소값 제외
                if min_hq:
                    exist[heapq.heappop(min_hq)[1]] = False
            elif num == 1:
                if max_hq:
                    exist[heapq.heappop(max_hq)[1]] = False

        while min_hq and not exist[min_hq[0][1]]: # 0번째가 exist하지 않으면 이미 빠진 것 -> 제거
            heapq.heappop(min_hq)
        while max_hq and not exist[max_hq[0][1]]:
            heapq.heappop(max_hq)

    if min_hq and max_hq:
        print(-max_hq[0][0], min_hq[0][0])
    else:
        print('EMPTY')