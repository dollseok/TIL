# SWEA 동철이의 일 분배

'''
N명의 직원
N개의 일
i번 직원이 j번 일을하면 성공할 확률이 P[i][j]
주어진 일이 모두 성공할 확률
'''

# import sys
# sys.stdin = open('input.txt', 'r')

def backtrack(arr,row):
    global success, mx
    if row > N-1:             # 가장 마지막 사람에게 일을 줬을 때 최대값인지 확인
        if mx < success:
            mx = success
        return
    if success < mx:          # 최대값을 구하는 건데 확률은 1보다 크지 않은 이상 곱할수록 작아진다.
        return

    for i in range(N):
        if visited[i] and arr[row][i] != 0:       # 0퍼센트면 하는 의미가 없으므로 넘어간다.
            success = success*(arr[row][i]/100)   # 성공할 확률을 곱해준다
            row += 1                              # 다음 사람 확인할 것
            visited[i] = 0                        # 일을 줫으면 다른 일감 확인 
            backtrack(arr,row)                    # 백트래킹
            row -= 1
            visited[i] = 1
            success = success/(arr[row][i]/100)

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [1]*N
    success = 1
    mx = 0

    backtrack(arr,0)
    print(f'#{test_case}', format(mx*100, '.6f'))    # 소수점 6번째까지 출력하는 format함수
