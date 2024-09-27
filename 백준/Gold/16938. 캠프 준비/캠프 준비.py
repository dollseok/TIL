'''

문제 N개 가지고 있고, 난이도 정수, i번쨰 문제 난이도는 Ai

두문제 이상

문제 난이도의 합은 L보다 크거나 같고 R보다 작거나 같다
가장 어려운 문제와 가장 쉬운 문제의 난이도 차이는 X보다 크거나 같아야한다.

N은 15이하

완전 탐색으로 구한다면

2문제 이상 고를건데
모두 선택하면 N
for 문으로 하나씩 골랐을때 sum의 값 범위, min,max 값 차이 구하기


'''

def recur(depth,idx,maxi,mini,tot):
    global cnt
    if tot > r:
        return
    elif depth >= 2 and l<= tot <= r:
        if maxi - mini >= x:
            cnt += 1

    for i in range(idx,n):

        if mini == None:
            recur(depth + 1, i + 1, arr[i], arr[i], tot + arr[i])
        else:
            recur(depth + 1, i + 1, arr[i], mini, tot + arr[i])

n,l,r,x = map(int,input().split())
arr = sorted(list(map(int,input().split())))

cnt = 0

recur(0,0,None,None,0)

print(cnt)

