# SWEA 2817번 부분 수열의 합
'''

'''

def backtrack(n,sum_):
    global ans
    
    # 가지치기
    if sum_ > K:
        return
    
    # 종료 조건
    if n == N:
        if sum_ == K:
            ans += 1
        return

    # 하부 출력
    backtrack(n+1, sum_+arr[n])
    backtrack(n+1, sum_)


T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))

    ans = 0
    backtrack(0,0)

    print(f'#{test_case} {ans}')