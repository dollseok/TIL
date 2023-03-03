# SWEA 5356번 의석이의 세로로 말해요

# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1,T+1):
    arr = [input() for _ in range(5)]   # str 그대로 받아서 리스트로 만듦

    mx_len = 0                         
    for i in arr:                            # 각 줄의 최대 길이 확인
        if mx_len < len(i):
            mx_len = len(i)

    res = ''
    for i in range(mx_len):              # 가장 긴것도 끝까지 읽음 
        for line in arr:                  
            if len(line) >= i + 1:         # 만약 그 줄이 확인하는 인덱스보다 길 때만 확인 
                res += line[i]

    print(f'#{test_case}', res)