# SWEA 2819번 격자판의 숫자 이어 붙이기
'''

'''

def dfs(n,ci,cj,st):
    if n == 7:
        set_.add(st)
        return

    for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
        ni = ci + di
        nj = cj + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(n+1, ni, nj, st + arr[ci][cj])


T = int(input())
for test_case in range(1,T+1):
    arr = [input().split() for i in range(4)]
    str_ = ''
    set_ = set()

    for i in range(4):
        for j in range(4):
            dfs(0, i, j, arr[i][j])

    print(f'#{test_case}', len(set_))