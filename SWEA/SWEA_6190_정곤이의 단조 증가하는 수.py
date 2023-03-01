# SWEA 6190번 정곤이의 단조 증가하는 수

'''
하나씩 곱한 것들을 리스트업하고 단조 증가하는 수인지 확인
'''

import sys
sys.stdin = open("input.txt", "r")


# 첫번째 풀이

'''
첫번째 풀이는 곱합것들의 리스트를 만들어서 그 숫자들을 str로 만든 다음에 sort를 이용해서 같은지 비교하려고 했지만
런타임 에러가 났음

최대한 줄여봐도 최대 49개까지임
'''

T = int(input().strip())
for test_case in range(1, T+1):
    N = int(input().strip())                             # 숫자의 개수
    nums = list(map(int, input().strip().split()))       # 숫자들 리스트
    multi_list = []

    for i in range(N-1):                         # 각 원소들 모두 곱해서 리스트로 받음
        for j in range(i+1, N):
            multi_list.append(nums[i]*nums[j])

    res = -1
    multi_list.sort()                            # 미리 정렬해서 뒤에서부터 받을 예정
    l = len(multi_list)

    for i in range(l-1,-1,-1):
        trans = str(multi_list[i])                # 문자열로 바꾸어서
        if list(trans) == sorted(list(trans)):    # 리스트로 만든후 sort한 것과 비교 후에 같으면
            res = multi_list[i]                   # 뒤에서부터 받았으니 옳은 것이 나오면 바로 최대값
            break

    print(f'#{test_case}', res)

# 두번째 풀이
'''
문자열로 바꾸는 것은 같지만 sort를 이용한것이 아니라 각 원소별로 하나씩 비교해서 
만약에 중간에라도 안맞는게 있으면 break를 걸어서 시간을 줄임

'''

T = int(input())
for test_case in range(1,T+1):
    N = int(input())                                  # 숫자의 개수
    nums = list(map(int, input().split()))            # 숫자들 리스트
    multi_list = []                                   # 다 곱한 것 리스트

    for i in range(N-1):
        for j in range(i+1, N):
            multi_list.append(str(nums[i]*nums[j]))   # 문자열로 바꾸어서 리스트에 추가

    # print(multi_list)
    max_res = -1                                      # 최대 결과 값 변수 ( 안나오면 -1 그대로 출력 )
    l = len(multi_list)
    for w in range(l):
        for k in range(len(multi_list[w]) - 1):       # 가장 뒤에서 -1해서 받아야 범위 안넘어감
            if multi_list[w][k] > multi_list[w][k+1]: # 앞에 숫자와 뒤에 숫자 비교했을 때 앞에 숫자가 크면 브레이크
                break
        else:
            if max_res < int(multi_list[w]):          # 최대값인지 확인
                max_res = int(multi_list[w])

    print(f'#{test_case}', max_res)