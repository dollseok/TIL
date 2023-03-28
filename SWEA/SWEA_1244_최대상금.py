# SWEA 1244번 최대 상금

'''
숫자 교환해서 가증 큰 큼액의 숫자를 계산해보자
최대 자릿수는 6자리, 최대 교환 횟수는 10번
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1,T+1):
    m, change_cnt = input().split()
    change_cnt = int(change_cnt)
    m_list = list(m)
    start = 0
    l = end = len(m_list)
    mx = max(m_list)
    mx_cnt = m_list.count(mx)

    if mx_cnt > change_cnt:                # 최대값의 개수가 교환 횟수보다 많으면 순서를 고려해서 바꾸어줘야함
        mn_list = []                       # 앞의 최대값이 나오기 전까지 작은 수들의 리스트를 만듦
        while m_list[start] != mx and start != change_cnt:
            # 첫 값이 mx값이거나(이 때는 바꿔도 의미 없으므로 start지점을 다음 지점부터 확인)
            # start값이 change_cnt 값과 같아지면 반복문 브레이크 (이 때는 교환 횟수를 다 채운 것이므로 끝)
            # 최대값들과 한번에 바꾸기 위한 작업
            mn_list.append(m_list[start])
            start += 1
        mn_list.sort(reverse=True)         # 역순으로 정렬해서 pop을 사용

        for i in range(l-1,-1,-1):         # 최대값을 뒤에서부터 확인 (그래야 가장 작은 자리수 쪽에 있는 최대값을 가장 큰 자리수로 옮길 수 있음)
            if m_list[i] == max(m_list):   # 최대값을 발견하면
                a = mn_list.pop()          # mn_list의 최소값과 먼저 바꿔줌
                m_list[m_list.index(a)], m_list[i] = m_list[i], m_list[m_list.index(a)]
            if not mn_list:                # mn_list가 더이상 없으면 break
                break

        res = m_list

    else:                                           # 최대값의 개수가 교환 횟수보다 작을 때
        highest = sorted(m_list, reverse=True)      # 최종적으로 갈 수 있는 가장 최대값

        while m_list != highest and change_cnt != 0:      # highest와 같아지면 다른 방식으로 최종 값 확인, 그리고 교환 횟수 끝나면 최종값 확인
            inst_list = m_list[start:]                    # 가장 앞이 고정되고 그 뒤에를 확인하려고 만든 임시 리스트
            if inst_list[end-start-1] == max(inst_list):  # 임시 리스트의 가장 뒤의 값이 max 값이면

                if m_list[start] != max(inst_list):       # 메인 리스트에서의 start지점이 임시리스트의 최대값과 다를 때
                    m_list[end-1], m_list[start] = m_list[start], m_list[end-1]   # 자리 교환
                    change_cnt -= 1                       # 교환 횟수 차감
                    start += 1                            # 시작 지점 + 1
                    end = l                               # 끝지점 다시 리셋
                else:                                     # 메인리스트에서 start지점이 최대값이면 바꾸는게 의미가 없음
                    start += 1                            # 시작 지점 다음으로 넘김
                    end = l                               # 끝지점 다시 리셋

            else:                                         # 임시리스트 가장 뒤의 값이 최대값이 아니면
                end -= 1                                  # 임시리스트 끝지점 하나 앞으로 땡겨서 확인

        # while문 끝나고 나왔을 떄
        # highest와 같아졌거나, 교환횟수가 끝난 상황

        # highest와 같아져서 나와서 교환횟수가 남았을 때
        if change_cnt != 0:
            if len(set(m_list)) != len(m_list):    # 중복되는 값이 있다면
                res = m_list                       # 중복 된 값끼리 바꿔주면 됨으로 결과값은 정해짐
            else:                                  # 중복되는 값이 없다면
                if change_cnt % 2 == 0:            # 짝수번의 change_cnt가 남았을 때
                    res = m_list                   # 짝수번 바꾸면 원상 복귀임으로 결과값 정해짐
                else:                              # change_cnt가 홀수번 남았을 때
                    m_list[-1], m_list[-2] = m_list[-2], m_list[-1]    # 가장 뒤의 값과 그 앞의 값을 바꿔주면 값이 크게 변하지 않고 끝남
                    res = m_list
        else:                 # 교환 횟수가 안남아서 나온 경우
            res = m_list

    print(f'#{test_case}', "".join(res))

