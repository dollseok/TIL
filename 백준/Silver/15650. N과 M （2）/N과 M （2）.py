'''

N과 M 2

1부터 N 까지 자연수중에서 중복 없이 M개
고른 수열은 오름 차순

4 2

1 2
1 3
1 4
2 3
2 4
3 4


'''

def recur(depth,current):
    if depth == m:
        print(*ls)
        return

    for i in range(1,n+1):
        if visited[depth] or current >= i: # 방문을 했다면 패스
            continue

        ls[depth] = i
        visited[depth] = True
        recur(depth + 1,i)
        visited[depth] = False


n,m = map(int,input().split())
ls = [0]* m
visited = [False] * (m+1)

recur(0,0)