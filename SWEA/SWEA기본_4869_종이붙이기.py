#SWEA 문제해결 기본 4869번 종이 붙이기

'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYXI5IoKVCoDFAQK&contestProbId=AYZNTmWK06sDFARc&probBoxId=AYXI6OVKVLsDFAQK&type=USER&problemBoxTitle=%EC%8B%A4%EC%8A%B5%28%EC%A1%B0%EB%B3%84%EB%B0%9C%ED%91%9C%29&problemBoxCnt=25

DP로 푸는 문제
나는 한칸한칸으로 풀었음
'''

import sys
sys.stdin = open("input.txt", "r")

def count_paper(n):
    if n == 1:         # 첫번째 값은 1 (20x10짜리 1개)
        return 1
    if n % 2:          # True라면 1이 나온 것이므로 홀수
        res = count_paper(n-1)*2 - 1
        return res
    else:              # 짝수번째라면
        res = count_paper(n-1)*2 + 1
        return res

T = int(input())
for test_case in range(1, T+1):
    N = int(input())//10 # 10으로 나눠줘야 몇번째인지 알 수 있음
    print(f'#{test_case} {count_paper(N)}')



# DP를 이용한 풀이

'''
tile(N) : 20xN 크기의 직사각형을 채우는 방법의 수

가장 끝부분만 채운다고 생각을 하고 
1칸짜리를 미리 채웟을 때 개수
tile(N-1) 개

2칸짜리를 미리 채웟을 때 개수
tile(N-2) * 2개

tile(N) = tile(N-1) + tile(N-2) * 2

tile(1) = 1
tile(2) = 3

tile(3) = 5 인것까지 편하게 알수 있다
'''
