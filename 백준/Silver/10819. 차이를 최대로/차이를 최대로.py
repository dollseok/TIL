'''

N개의 정수로 이루어진 배열 A

정수의 순서를 바꿔서 다음 식의 최댓값을 구하는 프로그램

숫자는 -100~100

|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

1. 완저탐색
모든 순서를 다 고려
중복 없이 모든 순서 고려한 숫자 입력

'''



n = int(input())

ls = list(map(int,input().split()))

order = [0] * n

visited = [False] * n

res = 0

def recur(depth):
    global res
    if depth == n:
        # 결과 확인
        tmp = 0
        for i in range(n-1):
            tmp += abs(order[i] - order[i+1])

        res = max(res,tmp)
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        order[depth] = ls[i]
        recur(depth + 1)
        visited[i] = False

recur(0)
print(res)