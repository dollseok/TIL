# SWEA 1952번 모의 SW 역량테스트. 수영장
'''

'''

def dfs(month, pay):
    global min_pay
    #가지 치기
    if pay > min_pay:
        return
    
    if month > 12:
        if min_pay > pay:
            min_pay = pay
        return

    dfs(month+1, pay + day*lst[month])
    dfs(month+1, pay + mon)
    dfs(month+3, pay + mon3)
    dfs(month+12, pay+year)


T = int(input())
for test_case in range(1,T+1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int,input().split()))

    min_pay = 3000*365
    dfs(1,0)

    print(f'#{test_case} {min_pay}')