# SWEA 2806번 N-Queen

'''
N*N 보드에 N의 퀸을 놓는다. 서로 다른 두 퀸이 서로 공격을 못하게 하는 경우의 수
'''

# import sys
# sys.stdin = open('input.txt','r')

def backtrack(arr, row, col):
    global cnt

    dr = [[-1, -1], [-1, 0], [-1, 1]]                  # 윗쪽방향에 1이 있는지 확인함
    for i in range(3):                                  
        ni, nj = row, col                              # 좌표값 정해줌
        di, dj = dr[i]                                 # 이동하는 방향
        while True:
            if 0 <= ni + di < N and 0 <= nj + dj < N:  # board 안이라면
                if arr[ni + di][nj + dj] == 1:         # 그 자리에 1이 있다면 
                    return                             # 이미 그 자리는 나가리임으로 패스
                ni = ni + di                           # 그 방향에 이어서 직선으로 확인
                nj = nj + dj
            else:                                      # board 끝까지 확인했다면
                break                                  # 안전한 것임으로 다음 방향 확인

    arr[row][col] = 1                                  # 모두 통과했을 때 그자리에 1 추가
    
    if row == N-1:              # while문을 통과하고 1이 들어갔는데 row가 마지막 줄이면
        cnt += 1                # 다 채워진 것이므로 cnt + 1
        return
    
    row += 1                    # 1이 채워지면 다음 줄 확인
    for i in range(N):          # 다음 줄의 각 col들을 확인
        backtrack(arr,row,i)
    row -= 1                    # 한 row를 다 확인했으면 다시 윗줄로
    arr[row][col] = 0           # 확인한 row는 다시 0으로 돌린다


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    array = [[0]*N for _ in range(N)]
    # print(array)
    cnt = 0

    for i in range(N):            # 가장 윗줄은 하나씩 들어감으로 그 기준으로 백트래킹을 각자 해줌      
        backtrack(array,0,i)

    print(f'#{test_case}', cnt)