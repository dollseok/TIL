#SWEA 4865번 글자수

import sys
sys.stdin = open("input.txt", "r")

def my_len(l):
    cnt = 0
    for _ in l:
        cnt += 1
    return cnt

T = int(input())
for test_case in range(1, T+1):
    p = list(input())    # ['X', 'Y', 'P', 'V']
    t = list(input())    # ['E', 'O', 'G', 'G', 'X', 'Y', 'P', 'V', 'S', 'Y']
    n = my_len(p)
    m = my_len(t)

    # 딕셔너리는 key 값이 중복이 안되기 때문에 value를 0으로 해서 만들어준다.
    # dict_p = {}
    # for i in p:
    #     dict_p[i] = 0
    dict_p = {p[i] : 0 for i in range(n)}    # 영범님 코드 참고한 딕셔너리 제작법

    # t에서 하나씩 pop으로 뒤에부터 꺼내와서 dict_p key값에 넣어준다
    for i in range(m):
        a = t.pop()
        if a in dict_p.keys():
            dict_p[a] += 1

    # dict_p의 value 최대값
    max_cnt = 0
    for i in dict_p.values():
        if max_cnt < i:
            max_cnt = i

    print(f'#{test_case} {max_cnt}')