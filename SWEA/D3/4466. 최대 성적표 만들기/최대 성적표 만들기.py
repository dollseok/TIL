T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    scores = list(map(int,input().split()))

    scores.sort()

    score_sum = 0
    for i in range(K):
        score_sum += scores[N-i-1]

    print(f'#{tc}', score_sum)