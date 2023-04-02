# SWEA 4012번 모의 역량 테스트 요리사

'''

식재료  i , j와 같이 요리하면 시너지 Sij
A,B 음식을 만들 때, 두 음식 간의 맛 차이가 최소가 되는 경우를 찾고 그 최솟값 출력하는 프로그램 작성

'''


# import sys
# sys.stdin = open('input.txt','r')

def check(comb):
    global ans   

    visited = [i for i in range(N)]  # 중복이 되면 안된다.
    
    for i in comb:
        visited[i] = -1  # 이미 선택된 재료 체크

    first_food = 0
    # 첫번째 음식에 대한 시너지값 총합
    for i in range(N // 2 - 1):
        for j in range(i + 1, N // 2):
            first_food += arr[comb[i]][comb[j]] + arr[comb[j]][comb[i]]

    other_comb = []
    for i in visited:
        if i != -1:
            other_comb.append(i)
            
    # 현재 조합에 포함되지 않은 나머지로 다른 조합을 만든다
    second_food = 0
    # 두번째 음식에 대한 시너지값 총합
    for i in range(N // 2 - 1):
        for j in range(i + 1, N // 2):
            second_food += arr[other_comb[i]][other_comb[j]] + arr[other_comb[j]][other_comb[i]]

    diff = abs(first_food - second_food)
    # 최소값 체크
    if ans > diff:
        ans = diff



def nCr_check(n,r,s):
    global ans
    
    if r == 0:
        # 조합이 정해지면 현 조합에 대한 차이가 최소값인지 체크한다.
        check(comb)

    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr_check(n, r-1, i+1)



T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # visited = [i for i in range(N)]    # 중복이 되면 안된다.
    ans = 60000
    # 절반을 딱 나눠서 전부 사용 하는것
    # 조합을 사용한다.
    A = [i for i in range(N)]
    comb = [0]*(N//2)
    nCr_check(N,N//2,0)


    print(f'#{test_case}', ans)
