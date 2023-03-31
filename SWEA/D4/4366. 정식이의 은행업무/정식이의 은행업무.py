# SWEA 정식이의 은행 업무
'''
금액 2진수와 3진수
한자리만을 잘못 기억하고 있다.
'''

def check(num2,num3):
    global ans
    rnum2 = 0
    rnum3 = 0

    for i in range(len(num2)):
        rnum2 += (2**(len(num2)-1 -i))*num2[i]

    for i in range(len(num3)):
        rnum3 += (3**(len(num3)-1 -i))*num3[i]

    if rnum2 == rnum3:
        ans = rnum2
        return

def dfs(num2, num3, i):

    if ans != -1:
        return

    if i == len(num3):
        return

    if num3[i] == 0:
        num3[i] = 1
        check(num2,num3)
        num3[i] = 2
        check(num2,num3)
        num3[i] = 0

    elif num3[i] == 1:
        num3[i] = 0
        check(num2, num3)
        num3[i] = 2
        check(num2, num3)
        num3[i] = 1

    else:
        num3[i] = 1
        check(num2, num3)
        num3[i] = 0
        check(num2, num3)
        num3[i] = 2

    dfs(num2,num3,i+1)


T = int(input())
for test_case in range(1,T+1):
    num2 = list(map(int, input()))
    num3 = list(map(int, input()))

    ans = -1

    for i in range(len(num2)):

        if num2[i] == 0:
            num2[i] = 1
            dfs(num2, num3, 0)
            num2[i] = 0

        else:
            num2[i] = 0
            dfs(num2, num3, 0)
            num2[i] = 1

    print(f'#{test_case} {ans}')