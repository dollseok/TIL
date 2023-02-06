# SWEA 6485번 삼성시의 버스노선

'''
Input
1      //테스트 케이스 개수
2      //첫 번째 테스트 케이스, N=2
1 3    // A1 = 1, B1 = 3
2 5    // A2 = 2, B2 = 5
5      // P = 5
1      // 이하 C1 = 1, C2 = 2, C3 = 3, C4 = 4, C5 = 5
2
3
4
5
'''

'''
Output
#1 1 2 2 1 1
'''

# 내 풀이
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    cnt = [0]*5001       # 정류장 리스트 cnt, count로 셌기 때문에 사용하는 것은 0-5001개를 해야 5000번째 정류장이 들어간다.
    N = int(input())     # 버스 노선의 개수
    for _ in range(N):
        A1, A2 = map(int, input().split())     # A1 A2는 버스 노선의 시작과 끝
        # A_lst = list(range(A1, A2+1))
        for i in range(A1, A2+1):     # 버스 노선의 시작과 끝에 대해서
            cnt[i] += 1               # 그 정류장을 지나가면 cnt 인덱스를 찾아서 그 자리에 1을 추가

    P = int(input())        # P개의 버스 정류장에 몇개의 버스 노선이 지나가는지 확인
    res = []     # 몇개씩 지나갔는지 결과를 받을 리스트
    for _ in range(P):
        C = int(input())
        res.append(cnt[C])

    print(f'#{test_case}', *res)

# 강의 풀이

# import sys
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     # N번 반복하면서 노선 입력, 빈도수 표시
#     cnts = [0]*5000
#     for _ in range(N):
#         S, E = map(int,input().split())
#         for i in range(S, E+1):
#             cnts[i] += 1
#
#     P = int(input())
#     alst = []
#     for _ in range(P):
#         p = int(input())
#         alst.append(cnts[p])
#
#     print(f'{test_case} {alst}')



