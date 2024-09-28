'''
N개의 자연수 중에서 M개를 고른 수열
같은수 여러번 가능

'''

def recur(depth):

    if depth == m:
        print(*perm)
        return

    for i in range(n):
        perm[depth] = ls[i]
        recur(depth + 1)


n,m = map(int,input().split())

ls = sorted(list(map(int,input().split())))

perm = [0]*m

recur(0)