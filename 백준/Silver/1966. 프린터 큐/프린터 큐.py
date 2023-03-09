# 백준 1966번 프린터 큐

'''
QUEUE, FIFO에 따라 인쇄
현재 가장 앞에 있는 문서 중요도 확인
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면
이 문서는 인쇄 안하고 가장 뒤에 재배치

A B C D
2 1 4 3

'''

T = int(input())
for i in range(T):
    N,M = map(int,input().split())            # N : 문서의 개수, 현재 M번째 놓인 것이 몇번째에 출력되는지 확인
    data = list(map(int,input().split()))     # 데이터 리스트
    data_idx = [i for i in range(N)]          # 순서 리스트
    # print(data)
    # print(data_idx)
    print_cnt = 0

    # M번째 데이터가 이 몇번째 프린트로 나오게 되는가?
    while True:
        mx = max(data)             # 데이터중에 우선순위 최대값 일때 프린트
        idx = data_idx.pop(0)      # data_idx와 data가 동시에 움직임
        d = data.pop(0)
        if d != mx:                # data 우선순위가 mx가 아닐 때
            data_idx.append(idx)   # 그대로 뒤에 붙임
            data.append(d)

        else:                      # 데이터 우선순위가 mx면 프린트
            print_cnt += 1
            if idx == M:           # idx가 원하던 번째 순서이면 끝
                break

    print(print_cnt)
