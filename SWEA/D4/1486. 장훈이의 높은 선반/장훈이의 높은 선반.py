# SWEA 1486번 장훈이의 높은 선반

'''
높이가 B인 선반
점원의 키는 Hi, 탑을 쌓아서 선반 위의 물건을 사용할 것

탑의 높이는 점원이 1명일 경우 그 점원의 카와 같고
2명 이상일 경우 탑을 만든 모든 점원의 키의 합과 같음

가장 낮은 탑의 높이
'''

def backtrack(n,sum_):
    global min_sum
    # 가지치기
    if sum_ >= min_sum:        # 합이 최소값을 넘어가면 리턴
        return
    if B == min_sum:           # B와 완전 일치하면 리턴
        return

    if n == N:                 # 리스트의 인덱스를 딱 넘어가서 마지막일 때
        if sum_ >= B:          # 합이 선반 높이를 넘어간다면
            min_sum = min(sum_, min_sum)    # 최소값인지 확인
        return

    backtrack(n+1, sum_ + lst[n])
    backtrack(n+1, sum_)



T = int(input())
for test_case in range(1,T+1):
    N,B = map(int,input().split())       # N 직원수, B 선반 높이
    lst = list(map(int,input().split()))

    sum_ = 0
    min_sum = 20*10000
    backtrack(0,sum_)
    ans = min_sum-B

    print(f'#{test_case} {ans}')