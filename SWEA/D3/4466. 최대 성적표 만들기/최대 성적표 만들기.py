T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    scores = list(map(int,input().split()))

    scores.sort(reverse=True)

    score_sum = 0
    for i in range(K):
        score_sum += scores[i]

    print(f'#{tc}', score_sum)