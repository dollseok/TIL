# SWEA 격자판의 숫자 이어 붙이기

'''
4x4 크기의 격자판
동서남북 인접한 네방향으로 여섯번 이동하면서 7자리의 숫자를 만드는데 다른 숫자의 개수
'''

def backtrack(arr, si, sj, str_):
    global dr

    # str_ += arr[si][sj]

    if len(str_) == 7:
        res_list.append(str_)
        return

    for di,dj in dr:
        if 0 <= si+di < 4 and 0 <= sj+dj < 4:
            # si += di
            # sj += dj
            backtrack(arr, si + di, sj + dj , str_ + arr[si][sj])
            # 위아래 내용들 다 없앨 수 있음 -> 내용들을 그 함수에 넣어주고 나오면 이미 끝난것이므로 버리게 된다.
            # si -= di
            # sj -= dj
            # str_ = str_[0:len(str_)]


T = int(input())
for test_case in range(1,T+1):
    arr = [list(input().split()) for _ in range(4)]
    dr = [[1,0], [0,1], [-1,0], [0,-1]]
    str_ = ''
    res_list = []

    for i in range(4):
        for j in range(4):
            backtrack(arr, i, j, str_)

    print(f'#{test_case}',len(set(res_list)))