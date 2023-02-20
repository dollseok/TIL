#SWEA 문제해결 기본 5099번 피자굽기

'''
N의 피자를 동시에 구울 수 있고
M개의 피자가 있음.
리스트 배열로 구현, pop,append사용
피자 한번 돌고 나오면 C // 2

'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())            # N은 화덕에 들어갈수 있는 피자의 개수/ M은 구워야할 피자의 개수
    pizza = list(map(int, input().split()))     # pizza 치즈 양의 리스트를 받음
    nameQ = [i+1 for i in range(M)]             # 피자의 번호
    fire = [0] * N                              # 불에 들어가는 피자의 개수에 따른 리스트
    new_Q = []                                  # 피자 치즈와 이름을 합해서 넣을 새로운 Queue

    for i in range(M):
        new_Q.append([nameQ[i], pizza[i]])      # [피자 번호, 치즈의 양]

    # 첫 세팅
    for i in range(N):                          # 처음에 들어갈 수 있는 피자 개수만큼
        fire[i] = (new_Q.pop(0))                # new_Q에서 첫번째 것을 pop해서 fire에 넣음

    while True:
        p = fire.pop(0)                         # fire에서 첫번째 것을 pop해서 피자 확인
        if p[1]//2 == 0:                        # p[1] : 치즈의 양에서 //2 했을 때 0이 되면
            if new_Q:                           # new_Q가 남아있다면
                fire.append(new_Q.pop(0))       # fire에 추가

        else:                                   # 치즈의 양이 아직 0보다 크면
            p[1] = p[1]//2                      # 치즈 절반 된 것으로 치즈의 양 수정하고
            fire.append(p)                      # 다시 fire의 뒷 부분에 넣어줌

        if len(fire) == 1:                      # fire에 피자가 하나만 남았다면
            break                               # while문을 끝내고

    print(f'#{test_case}', fire[0][0])          # fire에 마지막 남은 피자의 이름 출력