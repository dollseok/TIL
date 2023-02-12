#SWEA 3143번 가장빠른 문자열 타이핑

'''
문자열 A, 문자열 B가 주어진다
문자열 A를 타이핑하려고하는데 문자열 B가 저장되어 있어서 키 한번 누른것으로 B 전체를 타이핑 할 수 있다
A 전체를 타이핑 하기위해 키를 눌러야 하는 횟수 구하기


'''

import sys
sys.stdin = open("input.txt", "r")

def my_len(l):
    cnt = 0
    for _ in l:
        cnt += 1
    return cnt

T = int(input())
for test_case in range(1, T+1):
    t, p = input().split()    # t = text, p = pattern
    t_length = my_len(t)
    p_length = my_len(p)
    i = 0
    cnt = 0

    while i < t_length:       # text를 끝까지 확인할 것이기에 범위를 끝까지 설정
        j = 0                 # 문자열 B(pattern)에서 첫번째부터 늘 돌아야해서 리셋을 시켜줌

        # 남은 길이가 pattern 길이보다 짧다면 남은 길이 cnt에 추가해주고 break
        if t_length - i < p_length:
            cnt += t_length - i
            break

        # 패턴과 text의 첫 글자가 같을 때
        if p[j] == t[i]:
            for j in range(p_length - 1):
                # 패턴의 길이 만큼 확인 (첫단어는 확인했으니 1 빼줌)
                i += 1
                j += 1
                if p[j] == t[i]:    # 두번째 단어가 같으면 계속
                    continue
                elif p[j] != t[i]:  # 다르다면
                    cnt += j        # 같았던 것 만큼 카운트에 추가해주고 break
                    break

        # 패턴과 text의 첫 글자가 다를 때 - 그냥 넘어감
        else:
            i += 1
            cnt += 1

    print(f'#{test_case} {cnt}')
