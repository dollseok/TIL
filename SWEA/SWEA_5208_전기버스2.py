# SWEA 5208번 전기버스2

'''
한 줄에 정류장의 수 N, N-1의 각 정류장에 있는 배터리
'''

# import sys
# sys.stdin = open('input.txt', 'r')

def backtracking(arr,ni):   # 배터리 arr, 현재 위치 ni
    global cnt, min_cnt

    if ni + arr[ni] >= N-1:                  # 마지막 지점을 넘어갈수 있는 배터리가 된다면
        if min_cnt > cnt:                    # 최소 cnt였는지 확인
            min_cnt = cnt
        return
    else:
        if cnt > min_cnt:                    # 최소 cnt보다 커지면 확인하는 의미가 없으니 return
            return

    start_battery = arr[ni]                  # 새로 시작하는 그 위치의 배터리
    for i in range(start_battery,0,-1):      # 가장 멀리있는 것부터 확인
        cnt += 1
        backtracking(arr,ni + i)
        cnt -= 1


T = int(input())
for test_case in range(1,T+1):
    data = list(map(int,input().split()))
    N = data[0]
    battery_data = data[1:]
    min_cnt = 9999
    cnt = 0

    backtracking(battery_data,0)
    print(f'#{test_case}', min_cnt)