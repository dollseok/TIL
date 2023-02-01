# SWEA Gravity 문제

'''
문제 링크
https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AV10CSr6ABUCFAY2

상자들이 쌓여있는 방이 있다. 방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때, 
낙차가 가장 큰 상자를 구하여 그 낙차를 리턴하는 프로그램을 작성하시오

- 중력은 회전이 완료된 후 적응된다.

- 상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다

- 방의 가로 길이는 항상 100이며, 세로길이도 항상 100이다

- 즉 상자는 최소 0 최대 100 높이로 쌓을 수 있다.

'''

# import sys
# sys.stdin = open("input.txt", "r")

'''
input

3
9
7 4 2 0 0 6 0 7 0
9
7 4 2 0 0 6 7 7 0
20
52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53

output

#1 7
#2 6
#3 13
'''

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    B = list(map(int, input().split()))
    # print(B)
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if B[i] > B[j]:
                cnt += 1
        B[i] = cnt
        # print(B)

    maxV = B[0]
    for k in B:
        if B[k] > maxV:
            maxV = B[k]

    print(f'#{test_case} {maxV}')








