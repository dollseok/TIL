# baekjoon 9012번 괄호

'''

'''
# import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())
for i in range(N):
    data = list(input())
    res = 'YES'

    if len(data) % 2 != 0:
        res = 'NO'

    else:
        stack = []
        for j in data:
            if j == '(':
                stack.append(j)

            else:
                if not stack:
                    res = 'NO'
                    break

                if stack:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        res = 'NO'
                        break
        if stack:
            res = 'NO'

    print(res)