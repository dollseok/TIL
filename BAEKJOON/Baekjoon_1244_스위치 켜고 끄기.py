#Baekjoon 1244번 스위치 켜고 끄기

'''
남학생 1 : 스위치 번호가 자기가 받은수의 배수면 스위치 변경
여학생 2 : 자기가 받은 수와 같은 번호 붙은 스위치 중심
20칸 넘으면 한줄 아래에 프린트
'''

import sys
sys.stdin = open("input.txt", "r")

def turn(switch):                           # 스위치 바꿔주는 함수
    if switch == 0:
        return 1
    elif switch == 1:
        return 0

n = int(input())                            # 스위치의 개수 8
light = list(map(int, input().split()))     # 빛의 상태 list
Person = int(input())                       # 사람 수 Person
for i in range(Person):
    s, p = map(int, input().split())        # s : 성별, p : 위치

    if s == 1:                              # 남학생일 때
        for j in range(n//p):               # 남학생 위치의 배수 자리 스위치 바꿈
            light[p*(j+1)-1] = turn(light[p*(j+1)-1])

    elif s == 2:                            # 여학생일 때
        pl = pr = p - 1                     # 자기 자신의 위치부터 확인
        while True:
            pl = pl - 1                     # 왼쪽은 한칸 앞으로
            pr = pr + 1                     # 오른쪽은 한칸 뒤로
            if (pl < 0) or (pr > n-1):      # 범위 넘어가면
                pl = pl + 1                 # 되돌리기
                pr = pr - 1
                break
            if light[pl] != light[pr]:      # 대칭이 아니면
                pl = pl + 1                 # 되돌리기
                pr = pr - 1
                break

        for k in range(pl, pr+1):           # 범위 내에서
            light[k] = turn(light[k])       # 싹 바꿔줌

if n <= 20:                                 # C가 20 이하면
    print(*light)                           # 프린트

else:                                       # C가 20 넘으면 20개 단위로 프린트
    for i in range(n//20):
        print(*light[i * 20 : (i+1)*20])

    print(*light[(n//20)*20 : n])





# 이전 풀이

'''
반례
5
0 1 0 0 0
1
2 3

원래 답
0 1 1 0 0

내꺼 답
0 0 1 1 0
'''

#
# def turn(switch):
#     if switch == 0:
#         return 1
#     elif switch == 1:
#         return 0
#
# def toggle(ary, x):
#     ary[x] = (ary[x]+1)%2
#
# C = int(input())                            # 스위치의 개수 8
# light = list(map(int, input().split()))     # 빛의 상태 list
# Person = int(input())                       # 사람 수 Person
# for i in range(Person):
#     s, p = map(int, input().split())        # s : 성별, p : 위치
#
#     if s == 1:                              # 남학생일 때
#         for j in range(C//p):               # 남학생 위치의 배수 자리 스위치 바꿈
#             light[p*(j+1)-1] = turn(light[p*(j+1)-1])
#
#     elif s == 2:                            # 여학생일 때
#         pl = pr = p - 1                     # 자기 자신의 위치부터 확인
#         while True:
#             if light[pl] == light[pr] and (pl - 1 >= 0) and (pr + 1 < C):   # 좌우가 같고 범위를 넘어가지 않을 때
#                 pl = pl - 1                 # 왼쪽은 한칸 앞으로
#                 pr = pr + 1                 # 오른쪽은 한칸 뒤로
#             else:                           # 조건안맞으면
#                 break                       # 브레이크
#
#         for k in range(pl, pr+1):           # 대칭인 범위 내에서
#             light[k] = turn(light[k])       # 싹 바꿔줌
#
#
#
# # for i in range(0, C, 20):
# #     print(' '.join(map(str, light[i:i+20])))
#
#
# if C <= 20:                                 # C가 20 이하면
#     print(*light)                           # 프린트
#
# else:                                       # C가 20 넘으면 20개 단위로 프린트
#     for i in range(C//20):
#         print(*light[i * 20 : (i+1)*20])
#
#     print(*light[(C//20)*20 : C])
