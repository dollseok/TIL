# SWEA 5215번 햄버거 다이어트
'''
정해진 칼로리를 넘지않는 햄버거를 주문하여 먹으려한다
칼로리를 넘지 않는 score의 최대값
'''
def dfs(n,score,calo):
    global ans

    if calo >= L:
        return
    
    if n == N:
        if calo < L:
            ans = max(score, ans)
        return

    dfs(n+1, score, calo)
    dfs(n+1, score+lst[n][0], calo+lst[n][1])

T = int(input())
for test_case in range(1,T+1):
    N,L = map(int,input().split())
    # N :재료의 수, L : 제한 칼로리
    lst = [list(map(int,input().split())) for _ in range(N)]
    # lst[i][0] : 맛에 대한 점수, lst[i][1] : 칼로리

    ans = 0
    dfs(0,0,0)

    print(f'#{test_case} {ans}')