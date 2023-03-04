# Baekjoon 2491번 수열

'''
길어지면 길어지는대로 cnt
꺾이면 cnt 0 으로 초기화
다시 cnt
꺾일때마다 최대값 확인
'''


# import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())
lst = list(map(int,input().split()))

mx_cnt = 1
up_cnt = 1                      # 한개만 있어도 기본적으로 cnt = 1
down_cnt = 1
for i in range(1, len(lst)):    # 인덱스 에러 안나게 1부터 시작
    if lst[i-1] == lst[i]:      # 앞에 것과 비교했을 때 같으면 어느 방향으로 갈지 몰라서 up,down 둘 다 1 추가
        up_cnt += 1
        down_cnt += 1
    elif lst[i-1] < lst[i]:     # 커지는 방향이라면
        up_cnt += 1             # up에는 1추가
        down_cnt = 1            # down은 1로 초기화
    elif lst[i-1] > lst[i]:     # 작아지는 방향이라면
        down_cnt += 1           # down에는 1 추가
        up_cnt = 1              # up은 1로 초기화

    mx_cnt = max([mx_cnt, up_cnt, down_cnt])     # 최대값 갱신

print(mx_cnt)
