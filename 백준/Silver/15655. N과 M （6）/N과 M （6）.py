'''

N개의 자연수 중에서 M 개 고른 수열
고른 수열은 오름차순

1. 완전 탐색

n개 중에 하나씩 선택하는데 오름차순
중복 x

첫번째 자리 for 문
...
m번째 자리 for 문

'''

def recur(depth,min_idx):
    if depth == m:
        print(*perm)
        return

    for i in range(min_idx,n):
        if visited[i]:
            continue
        perm[depth] = ls[i]

        visited[i] = True
        recur(depth + 1,i)
        visited[i] = False



n,m = map(int,input().split())

ls = sorted(list(map(int,input().split())))

perm = [0]*m
visited = [False]*n

recur(0,0)