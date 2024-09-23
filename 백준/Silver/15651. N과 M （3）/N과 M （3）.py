'''
N과 M 3

1-N 자연수중에서 M개 고른 수열

같은 수 여러번 가능

제한 없이 돌림
깊이만 체크

'''


def recur(depth):
    if depth == m:
        print(*ls)
        return

    for i in range(1,n+1):
        ls[depth] = i
        recur(depth+1)


n,m = map(int,input().split())
ls = [0]*m
recur(0)