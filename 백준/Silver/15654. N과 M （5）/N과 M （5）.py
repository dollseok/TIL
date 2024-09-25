'''

N개 자연수와 자연수 M

길이가 M인 수열 구하는 프로그램
N개의 자연수는 모드 다름

N개중에 M개 고른 수열

중복되는 수열을 여러번 출력 x

수열은 사전 증가순으로 출력

백트래킹
1. M의 수만큼 index로 수열 만들고 정렬된 리스트에서 프린트


'''

def recur(depth):
    if depth == m:
        print(*ls)
        return

    for i in range(0,n):
        if visited[i]:
            continue

        ls[depth] = origin[i]
        visited[i] = True
        recur(depth + 1)
        visited[i] = False


n,m = map(int,input().split())

origin = sorted(list(map(int,input().split())))
visited = [False]*n
ls = [0] * m

recur(0)