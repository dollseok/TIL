import sys
sys.stdin = open('input.txt','r')

# SWEA 5250번 최소 비용

'''
0,0시작 N-1,N-1 도착
상하좌우칸으로만 이동 가능
기본적으로 한칸 이동에 연료 1 소모

'''

def bfs(ni,nj):
    dr = [(0, 1), (1, 0), (-1,0), (0,-1)]
    energy_arr[ni][nj] = 0
    queue = [(ni,nj)]

    while queue:
        si,sj = queue.pop(0)

        for di,dj in dr:
            energy = energy_arr[si][sj]
            if 0 <= si+di < N and 0 <= sj+dj < N:
                # 에너지 변동 사항
                if arr[si+di][sj+dj] >= arr[si][sj]:
                    energy += arr[si+di][sj+dj] - arr[si][sj] + 1
                else:
                    energy += 1

                # 경로에 따라 최소에너지를 넣어준다
                if energy_arr[si + di][sj + dj] > energy:
                    energy_arr[si + di][sj + dj] = energy
                    queue.append((si + di, sj + dj))


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    energy_arr = [[9000000] * N for _ in range(N)]

    bfs(0,0)

    print(energy_arr)
    print(f'#{test_case}', energy_arr[N-1][N-1])




