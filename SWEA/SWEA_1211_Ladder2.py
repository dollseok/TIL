#SWEA 1211번 ladder2

'''
모든 출발점을 검사
바닥까지 가장 짧은 이동거리

아래 풀이에서는 그렇게 풀지 않았지만
가장 첫번째에서 시작지점이 1인 지점의 인덱스를 리스트로 만들고 거기에서 인덱스를 뽑아서 쓰면 편하다

최종 길이를 알아야해서 이동할 때마다 cnt를 1 추가하는 방식으로 길이를 잼
'''


import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    test_case = int(input())
    ladder = list([0] + list(map(int, input().split())) + [0] for _ in range(100))
    res_dict = {}               # 시작점과 길이를 받을 딕셔너리

#     start_list = []
#     for j in range(1,101):
#         if ladder[0][j] == 1:
#             start_list.append(j)    # j는 시작 지점의 인덱스
#
#     for start in start_list:
#         cnt = 0
#         # ... 으로 시작

    for j in range(1, 101):     # 가로 모든 부분 확인 할것
        cnt = 0                 # 길이를 변수로 저장
        if ladder[0][j] == 1:   # 첫 시작이 1
            start = j - 1       # 제일 앞뒤에 [0]을 추가해줘서 -1 # 마지막에 시점을 불러오기 위해 start를 저장
            cnt += 1
            i = 1
            while i < 99:                       # i가 끝까지 갈때까지 확인
                if ladder[i][j+1] == 1:         # 오른쪽에 1이라면
                    j += 1
                    cnt += 1
                    while ladder[i][j+1] != 0:  # 0이 나오는 사다리 끝까지 가줌
                        j += 1
                        cnt += 1

                    i += 1                      # 사다리 끝 도착 후 한칸 내려줌
                    cnt += 1

                elif ladder[i][j-1] == 1:       # 왼쪽에 1이 있다면
                    j -= 1
                    cnt += 1
                    while ladder[i][j-1] != 0:  # 0이 나오는 사다리 끝까지 가줌
                        j -= 1
                        cnt += 1

                    i += 1                      # 사다리 끝 도착 후 한칸 내려줌
                    cnt += 1

                else:
                    i += 1                      # 양쪽에 1이 없으면 아래로 내려줌
                    cnt += 1

            res_dict[cnt] = start               # 딕셔너리에 시작점과 길이를 저장
            # 키값에 길이를 해준 이유는 길이가 동일할 때 뒤에 것이 저장되도록하기위함
            # 길이가 같을 때는 j가 큰값을 넣게되는데 순차적으로 했기때문에 가능

    mn = 1000
    for i in res_dict.keys():
        if mn > i:
            mn = i

    print(f'#{test_case} {res_dict[mn]}')


