'''

0~9까지 숫자 입력가능

N개의 부등호

'''
def check(i,j,k):
    if k == '<':
        if i > j:
            return False
    else:
        if i < j:
            return False

    return True

def recur(cur,num):
    if cur == n+1:
        result.append(num)
        return

    for i in range(10):
        if visited[i]:
            continue

        if cur == 0 or check(num[cur-1],str(i),ls[cur-1]):
            visited[i] = True
            recur(cur + 1,num + str(i))
            visited[i] = False

n = int(input())
ls = input().split()

arr = [0]*(n+1)
visited = [False] * 10
result = []

recur(0,'')
print(result[-1])
print(result[0])